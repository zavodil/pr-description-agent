# AI PR Description Bot

This agent is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using Artificial Intelligence. It integrates with GitHub webhooks to listen for specific events and interacts with the OpenAI API to create comprehensive PR descriptions based on code changes.

## Main Functions

*   **Automated PR Description Generation**: When a PR author comments `/describe` on a Pull Request, the bot fetches the PR's details and diff content. It then uses an AI model (OpenAI) to generate a structured and professional description.
*   **GitHub Integration**: Authenticates as a GitHub App to securely retrieve PR information (title, diff) and update the PR description.
*   **Webhook Security**: Verifies incoming GitHub webhook payloads using a shared secret to ensure authenticity and prevent unauthorized access.
*   **Configurable AI Model**: Allows selection of the OpenAI model used for description generation.

## How it Works

The bot operates as a FastAPI application, exposing a webhook endpoint.
1.  **Event Listening**: It listens for `issue_comment` events from GitHub.
2.  **Trigger Condition**: Upon receiving a comment, it checks if the comment contains the `/describe` command and if the comment author is the same as the Pull Request author.
3.  **Data Retrieval**: If the conditions are met, it obtains an installation access token for the specific repository and fetches the PR's title and its complete diff content from GitHub.
4.  **AI Generation**: The PR title and diff are sent to the configured OpenAI model, which generates a concise and professional PR description including "What changed", "Why", and "Technical details".
5.  **PR Update**: Finally, the generated description is used to update the body of the Pull Request on GitHub.

## Inputs

*   **HTTP Webhook (POST)**: Receives GitHub webhook payloads, specifically `issue_comment` events, at the `/webhook` endpoint.
*   **Environment Variables**: Configuration details for GitHub App credentials, OpenAI API keys, and application settings.

## Outputs

*   **GitHub Pull Request Update**: Modifies the description of the target Pull Request on GitHub.
*   **HTTP Response (JSON)**: Sends a JSON response back to GitHub indicating whether the webhook event was processed or ignored.
*   **Console/Logs**: Prints operational status and error messages.

## Environment Variables

The agent relies on the following environment variables for configuration:

*   **`GITHUB_APP_ID`**: The unique ID of the registered GitHub App.
*   **`GITHUB_PRIVATE_KEY_PATH`** or **`GITHUB_PRIVATE_KEY`**: Path to the GitHub App's private key file, or the key content directly.
*   **`GITHUB_WEBHOOK_SECRET`**: The secret token used to verify GitHub webhook signatures.
*   **`OPENAI_API_KEY`**: Your API key for authenticating with the OpenAI service.
*   **`OPENAI_BASE_URL`**: (Optional) The base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   **`DEFAULT_MODEL_NAME`**: (Optional) The name of the OpenAI model to use for generating descriptions (defaults to `gpt-4-turbo-preview`).
*   **`PORT`**: (Optional) The port on which the FastAPI application will listen (defaults to `8088`).