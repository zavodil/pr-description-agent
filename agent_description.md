### AI PR Description Bot

The AI PR Description Bot is a GitHub App designed to automate the generation of professional Pull Request descriptions using artificial intelligence. It integrates with GitHub webhooks to listen for specific events and leverages an AI model to create comprehensive PR summaries based on code changes.

#### Key Functions

*   **Automatic PR Description Generation**: Automatically generates a detailed PR description when a new pull request is opened, provided its body is empty or contains the `/ai-describe` command.
*   **On-Demand PR Description Generation**: Generates or updates a PR description when the PR author comments `/describe` on their pull request. The bot then deletes the triggering comment.
*   **GitHub Integration**: Interacts with the GitHub API to fetch pull request details (including diffs), update PR descriptions, and manage comments.
*   **AI-Powered Content Creation**: Utilizes OpenAI's language models to analyze code diffs and PR titles, crafting structured descriptions that include "What changed," "Why," and "Technical details."
*   **Secure Webhook Handling**: Verifies the authenticity of incoming GitHub webhook payloads using HMAC-SHA256 signatures to ensure security.
*   **Author Verification**: Processes commands only if they originate from the pull request author, enhancing security and control.

#### How it Works

The bot operates as a FastAPI web service that receives GitHub webhook events. Upon receiving a `pull_request` (opened) or `issue_comment` (created) event, it determines if a description needs to be generated. If so, it authenticates with GitHub as an App, retrieves the PR's diff content, sends it to an AI model for analysis and description generation, and then updates the pull request on GitHub with the generated text.

#### Inputs

*   **Medium**: HTTP POST requests
*   **Source**: GitHub Webhooks
*   **Content**: JSON payloads for `pull_request` events (action: `opened`) and `issue_comment` events (action: `created`).
*   **Headers**: `X-Hub-Signature-256` (for signature verification), `X-GitHub-Event` (for event type).

#### Outputs

*   **Medium**: HTTP PATCH requests to GitHub API, HTTP DELETE requests to GitHub API, HTTP POST requests to OpenAI API.
*   **Content**:
    *   Updated Pull Request descriptions on GitHub.
    *   Deletion of the `/describe` comment on GitHub.
    *   JSON responses to GitHub webhook calls indicating processing status.

#### Configuration

The agent requires the following environment variables for operation:

*   **`GITHUB_WEBHOOK_SECRET`**: A secret key for verifying GitHub webhook signatures.
*   **`GITHUB_APP_ID`**: The unique identifier for the registered GitHub App.
*   **`GITHUB_PRIVATE_KEY_PATH`**: (Optional) Path to the GitHub App's private key file.
*   **`GITHUB_PRIVATE_KEY`**: (Optional) The content of the GitHub App's private key, used as an alternative to `GITHUB_PRIVATE_KEY_PATH`.
*   **`OPENAI_API_KEY`**: Your API key for authenticating with the OpenAI service.
*   **`OPENAI_BASE_URL`**: (Optional) The base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   **`DEFAULT_MODEL_NAME`**: (Optional) The name of the AI model to use for description generation (defaults to `gpt-4-turbo-preview`).
*   **`PORT`**: (Optional) The port on which the FastAPI application will listen (defaults to `8000`).