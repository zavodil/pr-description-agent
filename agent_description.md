# AI PR Description Bot

The **AI PR Description Bot** is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using Artificial Intelligence. It listens for specific commands in PR comments and, upon activation, fetches PR details, generates a comprehensive description, and updates the PR on GitHub.

## Main Functions

*   **GitHub Webhook Listener**: Receives and processes GitHub webhook events, specifically `issue_comment` events.
*   **Secure Webhook Verification**: Verifies the authenticity of incoming GitHub webhooks using a secret key to ensure data integrity and origin.
*   **GitHub API Interaction**: Authenticates with GitHub as a GitHub App to obtain installation access tokens. It then uses these tokens to retrieve PR information (title, diff) and update the PR description.
*   **AI-Powered Description Generation**: Utilizes the OpenAI API to generate detailed and professional PR descriptions based on the PR's title and its code changes (diff). The generated description includes "What changed," "Why," and "Technical details."
*   **Automated PR Update**: Automatically updates the target Pull Request's description on GitHub with the AI-generated content.

## How it Works

The bot operates by monitoring `issue_comment` events on GitHub repositories where it is installed. When a Pull Request author adds a comment containing the `/describe` command, the bot performs the following steps:
1.  Verifies the webhook signature for security.
2.  Extracts the PR details (owner, repository, PR number, title, and diff content).
3.  Generates an installation access token for the GitHub App.
4.  Sends the PR title and diff content to the OpenAI API to generate a descriptive summary.
5.  Updates the Pull Request description on GitHub with the AI-generated text.

## Inputs

*   **Medium**: HTTP POST requests to the `/webhook` endpoint.
*   **Content**: GitHub webhook payloads (JSON), primarily `issue_comment` events.
*   **Headers**: `X-Hub-Signature-256` for webhook signature verification.

## Outputs

*   **Medium**:
    *   HTTP JSON responses to the GitHub webhook.
    *   GitHub API calls to update Pull Request descriptions.
*   **Content**:
    *   JSON responses indicating processing status (`'processed'` or `'ignored'`) and success (`true`/`false`).
    *   Updated Pull Request descriptions on GitHub, formatted in Markdown.
    *   Health check responses on `/` and `/health` endpoints.

## Environment Variables

The agent relies on the following environment variables for configuration and secure operation:

*   **`GITHUB_APP_ID`**: The unique identifier for the registered GitHub App.
*   **`GITHUB_PRIVATE_KEY_PATH`**: (Optional) Path to the file containing the GitHub App's private key.
*   **`GITHUB_PRIVATE_KEY`**: (Optional) Direct content of the GitHub App's private key. Used if `GITHUB_PRIVATE_KEY_PATH` is not provided or the file doesn't exist.
*   **`OPENAI_API_KEY`**: API key for authenticating with the OpenAI service.
*   **`OPENAI_BASE_URL`**: (Optional) Base URL for the OpenAI API. Defaults to `https://api.openai.com/v1`.
*   **`DEFAULT_MODEL_NAME`**: (Optional) The name of the AI model to use for description generation. Defaults to `gpt-4-turbo-preview`.
*   **`GITHUB_WEBHOOK_SECRET`**: A secret used to verify the authenticity of incoming GitHub webhook payloads.
*   **`PORT`**: (Optional) The port on which the FastAPI application listens. Defaults to `8088`.