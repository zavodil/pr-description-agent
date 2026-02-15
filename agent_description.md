**Agent Name**: AI PR Description Bot

**Description**:
The AI PR Description Bot is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using artificial intelligence. It integrates with GitHub via webhooks, allowing it to respond to specific commands within PR comments. When activated, it fetches PR details and diff content, leverages an AI model to craft a comprehensive description, and then automatically updates the PR on GitHub.

**Key Features**:
*   **GitHub Webhook Listener**: Monitors GitHub for `issue_comment` events, specifically looking for comments on Pull Requests.
*   **Secure Webhook Verification**: Ensures the authenticity and integrity of incoming GitHub webhook payloads using a shared secret.
*   **AI-Powered Description Generation**: Upon detecting a `/describe` command from the PR author, the bot retrieves the PR's title and diff. It then uses an OpenAI model to generate a structured description, outlining "What changed," "Why," and "Technical details."
*   **Automated PR Update**: Automatically updates the target Pull Request's description on GitHub with the newly generated AI content.
*   **GitHub App Authentication**: Authenticates with GitHub using a GitHub App's credentials to securely access PR information and perform updates.
*   **Health Check Endpoints**: Provides endpoints (`/` and `/health`) to verify the bot's operational status.

**Inputs**:
*   **GitHub Webhook Events**: HTTP POST requests to the `/webhook` endpoint, specifically `issue_comment` events where the comment is made by the PR author and contains the `/describe` command.

**Outputs**:
*   **GitHub Pull Request Updates**: HTTP PATCH requests to the GitHub API to update the description of a Pull Request.
*   **HTTP Responses**: JSON responses indicating the status of webhook processing and health checks.

**Configuration**:
The agent requires the following environment variables for proper operation:
*   `GITHUB_APP_ID`: Your GitHub App's unique identifier.
*   `GITHUB_PRIVATE_KEY_PATH` or `GITHUB_PRIVATE_KEY`: Path to or direct content of your GitHub App's private key.
*   `GITHUB_WEBHOOK_SECRET`: The secret used to verify GitHub webhook signatures.
*   `OPENAI_API_KEY`: Your OpenAI API key for accessing the AI model.
*   `OPENAI_BASE_URL` (Optional): Custom base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   `DEFAULT_MODEL_NAME` (Optional): The OpenAI model to use for generation (defaults to `gpt-4-turbo-preview`).
*   `PORT` (Optional): The port on which the FastAPI application listens (defaults to `8088`).