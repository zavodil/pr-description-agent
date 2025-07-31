### AI PR Description Bot

The AI PR Description Bot is a GitHub App designed to automate the generation and updating of Pull Request (PR) descriptions using artificial intelligence. It integrates with GitHub via webhooks and leverages an OpenAI-compatible API to create concise, professional descriptions based on the PR's title and code changes.

**Main Functions:**

*   **Automated PR Description Generation**: Automatically generates and updates PR descriptions when a new PR is opened, especially if the initial description is empty or contains the `/ai-describe` trigger.
*   **On-Demand PR Description Generation**: Allows PR authors to trigger description generation by commenting `/describe` on a PR. The bot will then update the PR description and delete the trigger comment.
*   **GitHub Integration**: Authenticates securely with GitHub using a GitHub App's private key to obtain installation tokens, allowing it to read PR details and update PR descriptions.
*   **AI-Powered Content Creation**: Utilizes an OpenAI-compatible API to analyze the PR's diff content and title, producing a structured description that includes what changed, why, and relevant technical details.
*   **Webhook Security**: Verifies the authenticity of incoming GitHub webhook payloads using a shared secret.

**Inputs:**

*   **HTTP**: GitHub webhook events (e.g., `pull_request.opened`, `issue_comment.created`) received at the `/webhook` endpoint.

**Outputs:**

*   **HTTP**: Updated GitHub Pull Request descriptions.
*   **HTTP**: JSON responses acknowledging webhook events and providing health status.

**Environment Variables:**

*   **`GITHUB_APP_ID`**: The ID of your registered GitHub App.
*   **`GITHUB_PRIVATE_KEY_PATH`**: (Optional) Path to the file containing the GitHub App's private key.
*   **`GITHUB_PRIVATE_KEY`**: (Optional) The content of the GitHub App's private key (can be multiline).
*   **`OPENAI_API_KEY`**: Your API key for authenticating with the OpenAI service.
*   **`OPENAI_BASE_URL`**: (Optional) The base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   **`DEFAULT_MODEL_NAME`**: (Optional) The name of the AI model to use for generating descriptions (defaults to `gpt-4-turbo-preview`).
*   **`GITHUB_WEBHOOK_SECRET`**: A secret token used to verify the authenticity of GitHub webhook payloads.
*   **`PORT`**: (Optional) The port on which the application will listen (defaults to `8000`).