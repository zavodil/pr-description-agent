# AI PR Description Bot

## Description
The AI PR Description Bot is a GitHub App designed to automate the generation of professional Pull Request descriptions using artificial intelligence. It integrates with GitHub webhooks and the OpenAI API to streamline the PR creation and review process by providing clear and concise summaries of code changes.

## Functionality
This agent automatically generates detailed Pull Request descriptions based on code changes. It operates in two primary modes:
*   **Automatic Generation**: When a new Pull Request is opened with an empty description or if its body contains the `/ai-describe` command, the bot will automatically fetch the PR's diff and generate a comprehensive description.
*   **On-Demand Generation**: A Pull Request author can trigger the description generation by commenting `/describe` on their PR. The bot will then replace the existing PR description with the AI-generated content and delete the trigger comment for a cleaner workflow.

The agent ensures secure communication by verifying GitHub webhook signatures and processes requests only from the original PR author for on-demand generation. It also provides health check endpoints for monitoring.

## Inputs
*   **GitHub Webhook Events (HTTP POST to `/webhook`)**:
    *   `pull_request.opened`: Triggered when a new pull request is opened.
    *   `issue_comment.created`: Triggered when a comment is made on an issue or pull request, specifically looking for `/describe` commands from the PR author.

## Outputs
*   **Updated GitHub Pull Request Description (via GitHub API)**: The agent modifies the body of the target Pull Request with the AI-generated content.
*   **HTTP JSON Response (HTTP)**: Acknowledges received webhook events and indicates processing status.
*   **Console Logs (stdout)**: Provides operational status and debugging information.

## Configuration
The agent requires the following environment variables to function:
*   `GITHUB_WEBHOOK_SECRET`: Used to verify the authenticity of incoming GitHub webhook payloads.
*   `GITHUB_APP_ID`: The unique identifier for the registered GitHub App.
*   `GITHUB_PRIVATE_KEY_PATH` or `GITHUB_PRIVATE_KEY`: Specifies either the file path to or the direct content of the GitHub App's private key, essential for authentication.
*   `OPENAI_API_KEY`: The API key for authenticating requests made to the OpenAI service.
*   `OPENAI_BASE_URL`: (Optional) The base URL for the OpenAI API endpoints (defaults to `https://api.openai.com/v1`).
*   `DEFAULT_MODEL_NAME`: (Optional) Defines the specific OpenAI model to be used for generating PR descriptions (defaults to `gpt-4-turbo-preview`).
*   `PORT`: (Optional) The network port on which the FastAPI application will listen for incoming requests (defaults to `8000`).