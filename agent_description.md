### AI PR Description Bot

The AI PR Description Bot is a GitHub App designed to automate the generation of Pull Request descriptions using Artificial Intelligence. It integrates with GitHub via webhooks and utilizes OpenAI's language models to create comprehensive and professional PR descriptions based on the changes in the pull request.

#### Main Functions

*   **Automated Description Generation**: Automatically generates and updates a PR description when a new Pull Request is opened, especially if its body is empty or contains the `/ai-describe` trigger.
*   **On-Demand Description Generation**: Allows PR authors to trigger description generation by commenting `/describe` on a Pull Request. The bot will then update the PR description and delete the trigger comment.
*   **GitHub Integration**: Interacts with the GitHub API to fetch PR details, retrieve diff content, and update PR descriptions.
*   **Secure Webhook Handling**: Verifies incoming GitHub webhook signatures to ensure the authenticity and integrity of events.
*   **AI-Powered Content Creation**: Leverages OpenAI's API to analyze PR diffs and titles, producing structured descriptions that include what changed, why, and technical details.

#### Inputs

*   **HTTP**: GitHub webhook events (JSON payload) sent to the `/webhook` endpoint, specifically `pull_request` and `issue_comment` events.

#### Outputs

*   **GitHub API**: Updates to Pull Request descriptions.
*   **GitHub API**: Deletion of trigger comments on Pull Requests.
*   **HTTP**: JSON responses indicating the status of webhook processing.

#### Environment Variables

The agent requires the following environment variables for configuration and operation:

*   **`GITHUB_APP_ID`**: The unique identifier for your GitHub App.
*   **`GITHUB_PRIVATE_KEY_PATH`** or **`GITHUB_PRIVATE_KEY`**: Path to the GitHub App's private key file, or the key content directly.
*   **`GITHUB_WEBHOOK_SECRET`**: The secret used to verify incoming GitHub webhook payloads.
*   **`OPENAI_API_KEY`**: Your API key for authenticating with the OpenAI service.
*   **`OPENAI_BASE_URL`** (Optional): The base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   **`DEFAULT_MODEL_NAME`** (Optional): The OpenAI model to use for generating descriptions (defaults to `gpt-4-turbo-preview`).
*   **`PORT`** (Optional): The port on which the FastAPI application will listen (defaults to `8000`).