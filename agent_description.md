### AI PR Description Bot

This agent is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using Artificial Intelligence. It integrates with GitHub via webhooks and leverages the OpenAI API to create comprehensive descriptions based on PR changes.

**Main Functions:**

*   **Automatic PR Description Generation:** For newly opened PRs, the bot can automatically generate a description if the PR body is empty or contains the `/ai-describe` trigger.
*   **On-Demand PR Description Generation:** PR authors can trigger the bot to generate or update a PR description by commenting `/describe` on the pull request. After processing, the bot deletes this command comment.
*   **GitHub Integration:** Authenticates as a GitHub App to securely fetch PR details (such as title and diff content) and update PR descriptions.
*   **AI-Powered Content Creation:** Utilizes the OpenAI API to analyze the PR's git diff and title, then generates a structured description covering "What changed," "Why," and "Technical details."
*   **Security:** Verifies GitHub webhook signatures to ensure the authenticity of incoming requests.

**Inputs:**

*   **GitHub Webhook Events (HTTP POST):** Receives `pull_request` events (for new PRs) and `issue_comment` events (for `/describe` commands) from GitHub.

**Outputs:**

*   **GitHub API Calls (HTTP):** Sends requests to the GitHub API to:
    *   Update Pull Request descriptions.
    *   Retrieve Pull Request information and diff content.
    *   Delete command comments.
*   **HTTP Responses (HTTP):** Returns JSON responses to GitHub indicating the status of webhook processing.
*   **Console Logs (stdout):** Provides operational and debugging information.

**Environment Variables:**

*   `GITHUB_APP_ID`: The ID of the registered GitHub App.
*   `GITHUB_PRIVATE_KEY_PATH` or `GITHUB_PRIVATE_KEY`: Path to the GitHub App's private key file, or the key content directly.
*   `GITHUB_WEBHOOK_SECRET`: The secret used to verify incoming GitHub webhook signatures.
*   `OPENAI_API_KEY`: Your API key for accessing OpenAI services.
*   `OPENAI_BASE_URL` (Optional): The base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   `DEFAULT_MODEL_NAME` (Optional): The OpenAI model to use for generating descriptions (defaults to `gpt-4-turbo-preview`).
*   `PORT` (Optional): The port on which the FastAPI application will run (defaults to `8000`).