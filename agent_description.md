### AI PR Description Bot

This agent is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using artificial intelligence. It integrates with GitHub to monitor PR events and leverages AI models to create comprehensive and professional descriptions based on code changes.

**Key Features:**

*   **Automatic PR Description Generation:** Automatically generates a PR description when a new pull request is opened, especially if its body is empty or contains a specific trigger phrase (`/ai-describe`).
*   **On-Demand Description Generation:** Allows PR authors to trigger description generation by commenting `/describe` on their pull request. The bot will then update the PR description and delete the trigger comment.
*   **GitHub Integration:** Interacts with the GitHub API to fetch PR details, retrieve code diffs, update PR descriptions, and manage comments.
*   **AI-Powered Content:** Utilizes OpenAI's language models to analyze code differences and PR titles to generate structured descriptions, including "What changed," "Why," and "Technical details" sections.
*   **Secure Webhook Handling:** Verifies incoming GitHub webhook signatures to ensure the authenticity and integrity of events.

**Inputs:**

*   **HTTP (GitHub Webhook):** Receives `pull_request.opened` and `issue_comment.created` events from GitHub.

**Outputs:**

*   **HTTP (GitHub API):** Updates the body of GitHub Pull Requests with AI-generated descriptions.
*   **HTTP (GitHub API):** Deletes the `/describe` command comment after processing.
*   **HTTP (JSON):** Responds to GitHub webhook events with processing status.

**Configuration:**

Requires environment variables for GitHub App authentication (ID, private key, webhook secret) and OpenAI API access (API key, base URL, model name).