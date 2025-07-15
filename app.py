import os
import json
import hmac
import hashlib
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional

from github_client import GitHubClient
from openai_client import OpenAIClient
from auth import GitHubAuth

load_dotenv()

app = FastAPI(
    title="AI PR Description Bot",
    description="GitHub App that generates PR descriptions using AI",
    version="0.1.0"
)


class WebhookPayload(BaseModel):
    action: str
    comment: Optional[dict] = None
    issue: Optional[dict] = None
    installation: Optional[dict] = None


class PRDescriptionBot:
    def __init__(self):
        self.webhook_secret = os.getenv('GITHUB_WEBHOOK_SECRET')
        self.github_auth = GitHubAuth()
        self.openai_client = OpenAIClient()

    def verify_webhook_signature(self, payload: bytes, signature: str) -> bool:
        """Verify GitHub webhook signature for security"""
        if not self.webhook_secret:
            return False

        expected_signature = hmac.new(
            self.webhook_secret.encode(),
            payload,
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(f'sha256={expected_signature}', signature)

    def is_pr_author_or_authorized(self, event: dict) -> bool:
        """Check if comment author can trigger description generation"""
        comment_author_id = event['comment']['user']['id']
        comment_author_login = event['comment']['user']['login']
        pr_author_id = event['issue']['user']['id']
        pr_author_login = event['issue']['user']['login']
        repo_owner_id = event['repository']['owner']['id']

        # Allow if commenter is PR author
        if comment_author_id == pr_author_id:
            return True

        # Allow if commenter is repository owner
        if comment_author_id == repo_owner_id:
            return True

        print(f"Comment by {comment_author_login} on PR by {pr_author_login} - not authorized")
        return False

    def should_process_comment(self, event: dict) -> bool:
        """Check if we should process this comment"""
        # Must be a PR comment
        if not event['issue'].get('pull_request'):
            return False

        # Must contain /describe command
        if '/describe' not in event['comment']['body']:
            return False

        # Check authorization
        if not self.is_pr_author_or_authorized(event):
            return False

        return True

    def should_auto_generate(self, event: dict) -> bool:
        """Check if we should auto-generate description for new PR"""
        # Must be a PR
        if not event.get('pull_request'):
            return False

        # Must be opened action
        if event.get('action') != 'opened':
            return False

        # Check if description is empty or contains trigger
        pr_body = event['pull_request'].get('body') or ''  # Handle None
        pr_body = pr_body.strip()

        # Auto-generate if empty or contains /ai-describe
        return not pr_body or '/ai-describe' in pr_body

    async def process_new_pr(self, event: dict) -> bool:
        """Process newly opened PR and generate description"""
        try:
            # Extract PR info
            if 'installation' not in event:
                print("No installation found in PR event")
                return False

            installation_id = event['installation']['id']
            pr = event['pull_request']
            owner = pr['base']['repo']['owner']['login']
            repo = pr['base']['repo']['name']
            pr_number = pr['number']

            print(f"Processing new PR {owner}/{repo}#{pr_number}")

            # Get installation token
            token = await self.github_auth.get_installation_token(installation_id)
            if not token:
                print(f"Failed to get installation token for {installation_id}")
                return False

            # Initialize GitHub client
            github = GitHubClient(token)

            # Get PR diff
            diff_content = await github.get_pr_diff(owner, repo, pr_number)

            if not diff_content:
                print(f"Failed to get PR diff for {owner}/{repo}#{pr_number}")
                return False

            # Generate description
            description = await self.openai_client.generate_description(
                diff_content, pr['title']
            )

            if not description:
                print(f"Failed to generate description for {owner}/{repo}#{pr_number}")
                return False

            # Update PR
            success = await github.update_pr_description(owner, repo, pr_number, description)

            if success:
                print(f"Auto-generated description for new PR {owner}/{repo}#{pr_number}")
                return True
            else:
                print(f"Failed to update new PR {owner}/{repo}#{pr_number}")
                return False

        except Exception as e:
            print(f"Error processing new PR: {e}")
            import traceback
            traceback.print_exc()
            return False

    async def process_pr_comment(self, event: dict) -> bool:
        """Process PR comment and generate description"""
        try:
            # Extract PR info
            pr_url = event['issue']['pull_request']['url']
            installation_id = event['installation']['id']
            comment_id = event['comment']['id']

            # Parse owner, repo, pr_number from URL
            parts = pr_url.split('/')
            owner = parts[-4]
            repo = parts[-3]
            pr_number = int(parts[-1])

            # Get installation token
            token = await self.github_auth.get_installation_token(installation_id)
            if not token:
                print(f"Failed to get installation token for {installation_id}")
                return False

            # Initialize GitHub client
            github = GitHubClient(token)

            # Get PR diff and info
            pr_info = await github.get_pr_info(owner, repo, pr_number)
            diff_content = await github.get_pr_diff(owner, repo, pr_number)

            if not pr_info or not diff_content:
                print(f"Failed to get PR data for {owner}/{repo}#{pr_number}")
                return False

            # Generate description
            description = await self.openai_client.generate_description(
                diff_content, pr_info['title']
            )

            if not description:
                print(f"Failed to generate description for {owner}/{repo}#{pr_number}")
                return False

            # Update PR
            success = await github.update_pr_description(owner, repo, pr_number, description)

            if success:
                # Delete the /describe comment
                await github.delete_comment(owner, repo, comment_id)
                print(f"Successfully updated PR {owner}/{repo}#{pr_number} and deleted comment")
                return True
            else:
                print(f"Failed to update PR {owner}/{repo}#{pr_number}")
                return False

        except Exception as e:
            print(f"Error processing PR comment: {e}")
            return False


bot = PRDescriptionBot()


@app.post("/webhook")
async def webhook(request: Request):
    """Handle GitHub webhook events"""
    signature = request.headers.get('X-Hub-Signature-256')
    payload = await request.body()

    # Verify webhook signature
    if not bot.verify_webhook_signature(payload, signature):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid signature"
        )

    try:
        event = json.loads(payload)

        # Debug logging
        event_type = request.headers.get('X-GitHub-Event', 'unknown')
        action = event.get('action', 'no_action')
        print(f"Received webhook: {event_type}.{action}")

        # Process issue comment events (manual /describe)
        if event.get('action') == 'created' and 'comment' in event:
            if bot.should_process_comment(event):
                success = await bot.process_pr_comment(event)
                return JSONResponse(
                    content={'status': 'comment_processed', 'success': success}
                )

        # Process new PR events (auto-generate)
        if 'pull_request' in event and bot.should_auto_generate(event):
            success = await bot.process_new_pr(event)
            return JSONResponse(
                content={'status': 'pr_auto_generated', 'success': success}
            )

        return JSONResponse(content={'status': 'ignored', 'event': f"{event_type}.{action}"})

    except Exception as e:
        print(f"Webhook error: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal error"
        )


@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {"status": "AI PR Description Bot is running", "version": "0.1.0"}


@app.get("/health")
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "ai-pr-description-bot",
        "version": "0.1.0"
    }


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get('PORT', 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)