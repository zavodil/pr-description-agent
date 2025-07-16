### AI PR Description Bot

This agent is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using Artificial Intelligence. It integrates with GitHub via webhooks and leverages OpenAI's API to create concise, professional, and informative PR descriptions based on the changes introduced in a pull request.

#### Functionality

*   **Automated PR Description Generation:** Automatically generates a detailed PR description when a new pull request is opened, especially if its body is empty or contains the `/ai-describe` keyword.
*   **On-Demand Description Generation:** Allows PR authors to trigger description generation by commenting `/describe` on a pull request. After generation, the trigger comment is automatically deleted.
*   **Secure Webhook Handling:** Verifies incoming GitHub webhook payloads using a shared secret to ensure authenticity and prevent unauthorized access.
*   **GitHub API Interaction:** Fetches PR details, diff content, and updates the PR description directly on GitHub.
*   **AI-Powered Content Creation:** Utilizes a configurable OpenAI model (defaulting to `gpt-4-turbo-preview`) to analyze code differences and PR titles, then crafts a description covering "What changed," "Why," and "Technical details."

#### Inputs

*   **HTTP Webhook Events:**
    *   GitHub `pull_request.opened` events (for automatic description generation).
    *   GitHub `issue_comment.created` events (for manual description generation via `/describe` command).

#### Outputs

*   **GitHub PR Updates:** Modified Pull Request descriptions on GitHub.
*   **GitHub Comment Deletion:** Removal of the `/describe` command comment after successful processing.
*   **HTTP Responses:** JSON responses indicating the status of webhook processing (e.g., `comment_processed`, `pr_auto_generated`, `ignored`).

#### Configuration (Environment Variables)

The agent requires the following environment variables for operation:

*   **`GITHUB_APP_ID`**: The unique ID of your GitHub App.
*   **`GITHUB_PRIVATE_KEY_PATH`** or **`GITHUB_PRIVATE_KEY`**: Path to the GitHub App's private key file, or the key content directly.
*   **`GITHUB_WEBHOOK_SECRET`**: The secret used to verify GitHub webhook signatures.
*   **`OPENAI_API_KEY`**: Your API key for authenticating with OpenAI services.
*   **`OPENAI_BASE_URL`** (Optional): The base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   **`DEFAULT_MODEL_NAME`** (Optional): The OpenAI model to use for generation (defaults to `gpt-4-turbo-preview`).
*   **`PORT`** (Optional): The port on which the application listens (defaults to `8000`).