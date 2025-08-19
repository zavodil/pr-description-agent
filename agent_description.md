### AI PR Description Bot

This agent is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using artificial intelligence. It integrates with GitHub to monitor PR activities and leverages an AI model to create informative and professional descriptions based on code changes.

**Main Functions:**

*   **Automatic PR Description Generation:** Automatically generates a description for newly opened Pull Requests if their body is empty or contains the `/ai-describe` command.
*   **On-Demand PR Description Generation:** Allows a Pull Request author to trigger description generation by commenting `/describe` on their PR.
*   **GitHub Integration:** Interacts with the GitHub API to fetch PR details, retrieve code diffs, update PR descriptions, and delete trigger comments.
*   **AI-Powered Content Creation:** Utilizes an OpenAI model to analyze PR diffs and titles, then generates a structured description including "What changed," "Why," and "Technical details."
*   **Security:** Verifies incoming GitHub webhook signatures to ensure authenticity and processes commands only from the PR author.

**Inputs:**

*   **HTTP (POST /webhook):** Receives GitHub webhook events, primarily `pull_request` events (for new PRs) and `issue_comment` events (for `/describe` commands).

**Outputs:**

*   **GitHub API:** Updates the body/description of a Pull Request.
*   **HTTP:** Responds to GitHub webhook calls with status acknowledgments and provides health check responses.

**Configuration:**

The agent requires the following environment variables for proper operation:

*   `GITHUB_APP_ID`: Your GitHub App's unique identifier.
*   `GITHUB_WEBHOOK_SECRET`: The secret key used to verify the authenticity of GitHub webhook payloads.
*   `GITHUB_PRIVATE_KEY_PATH` or `GITHUB_PRIVATE_KEY`: The private key for your GitHub App, used for authentication with the GitHub API.
*   `OPENAI_API_KEY`: Your API key for authenticating requests to OpenAI services.
*   `OPENAI_BASE_URL`: (Optional) Specifies the base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   `DEFAULT_MODEL_NAME`: (Optional) Sets the default AI model to use for description generation (defaults to `gpt-4-turbo-preview`).
*   `PORT`: (Optional) The port on which the agent's web server will listen (defaults to `8000`).

**Permissions:**

This GitHub App requires the following permissions to function:

*   **Pull requests:** Write (to update PR descriptions).
*   **Issues:** Read (to read PR comments).
*   **Contents:** Read (to access code diffs).
*   **Metadata:** Read (for basic repository access).