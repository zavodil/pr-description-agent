### AI PR Description Bot

The AI PR Description Bot is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using Artificial Intelligence. It integrates with GitHub to listen for specific events and uses an OpenAI model to create concise and professional PR summaries based on code changes.

#### Functionality

This agent performs the following key functions:

*   **Automated PR Description Generation:** Automatically generates and updates the description for newly opened Pull Requests if their body is empty or contains the `/ai-describe` trigger.
*   **On-Demand PR Description Generation:** Allows users to manually trigger PR description generation by commenting `/describe` on an existing Pull Request. The bot will then update the PR description and delete the trigger comment.
*   **GitHub Integration:** Authenticates as a GitHub App to securely interact with the GitHub API, fetching PR details, diffs, and updating PRs.
*   **AI-Powered Content Creation:** Leverages OpenAI's language models to analyze code differences and PR titles, crafting structured descriptions that include "What changed," "Why," and "Technical details."
*   **Webhook Security:** Verifies incoming GitHub webhook signatures to ensure the authenticity and integrity of events.

#### Inputs

*   **Medium:** HTTP POST requests (GitHub Webhooks)
*   **Details:**
    *   **`pull_request` events with `opened` action:** Trigger automated description generation if the PR body is empty or contains `/ai-describe`.
    *   **`issue_comment` events with `created` action:** Trigger on-demand description generation if the comment is on a Pull Request, from the PR author, and contains `/describe`.
    *   Requires `X-Hub-Signature-256` header for webhook payload verification.

#### Outputs

*   **Medium:** HTTP JSON responses, GitHub API calls, stdout logs
*   **Details:**
    *   Updates the description of GitHub Pull Requests.
    *   Deletes the `/describe` command comment after successful processing.
    *   Returns JSON responses to GitHub webhook calls indicating processing status.
    *   Logs operational information and errors to standard output.

#### Configuration (Environment Variables)

The agent requires the following environment variables for proper operation:

*   **`GITHUB_APP_ID`**: The unique ID of your registered GitHub App.
*   **`GITHUB_PRIVATE_KEY_PATH`** or **`GITHUB_PRIVATE_KEY`**: The file path to, or the content of, your GitHub App's private key. The file path takes precedence if both are provided.
*   **`GITHUB_WEBHOOK_SECRET`**: The secret token configured for your GitHub App's webhooks, used for signature verification.
*   **`OPENAI_API_KEY`**: Your API key for authenticating with the OpenAI service.
*   **`OPENAI_BASE_URL`** (Optional): The base URL for the OpenAI API. Defaults to `https://api.openai.com/v1`.
*   **`DEFAULT_MODEL_NAME`** (Optional): The name of the OpenAI model to use for generating descriptions. Defaults to `gpt-4-turbo-preview`.
*   **`PORT`** (Optional): The port on which the FastAPI application will listen for incoming requests. Defaults to `8000`.