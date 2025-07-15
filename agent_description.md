### AI PR Description Bot

The AI PR Description Bot is a GitHub App designed to automate the generation of Pull Request (PR) descriptions using artificial intelligence. It integrates with GitHub via webhooks and leverages an OpenAI model to create concise and professional PR summaries based on the code changes.

**Main Functions:**
*   **Automatic Description Generation:** Automatically generates and updates the PR description when a new Pull Request is opened, provided its description is empty or contains the `/ai-describe` trigger phrase.
*   **On-Demand Description Generation:** Generates and updates the PR description when the PR author adds a comment containing `/describe` to an existing Pull Request. After successful generation, the trigger comment is automatically deleted.
*   **GitHub Integration:** Authenticates as a GitHub App to fetch PR details (title, diff content) and update the PR's body.
*   **AI-Powered Summarization:** Utilizes an OpenAI model to analyze the PR's diff and title, producing a structured description that includes "What changed," "Why," and "Technical details" in markdown format.

**How it Works:**
The bot listens for specific GitHub webhook events:
1.  **`pull_request.opened`**: Triggers automatic description generation if the PR body is empty or contains `/ai-describe`.
2.  **`issue_comment.created`**: Triggers on-demand description generation if the comment is from the PR author and contains `/describe`.

**Inputs:**
*   **Medium:** HTTP POST requests (GitHub Webhooks)
*   **Content:** GitHub webhook payloads for `pull_request` events (specifically `opened` action) and `issue_comment` events (specifically `created` action). These payloads contain details such as repository owner, repository name, PR number, PR title, PR body, comment content, and installation ID.

**Outputs:**
*   **Medium:** HTTP responses to GitHub webhook calls; API calls to GitHub; API calls to OpenAI.
*   **Content:**
    *   Updates the Pull Request description on GitHub with the AI-generated content.
    *   Deletes the `/describe` comment from the Pull Request after successful processing.
    *   JSON responses indicating the processing status of the webhook event.

**Configuration (Environment Variables):**
The bot requires the following environment variables for proper operation:
*   `GITHUB_APP_ID`: Your GitHub App's unique ID.
*   `GITHUB_PRIVATE_KEY_PATH` or `GITHUB_PRIVATE_KEY`: Path to your GitHub App's private key file, or the key content directly.
*   `OPENAI_API_KEY`: Your OpenAI API key for accessing the AI model.
*   `GITHUB_WEBHOOK_SECRET`: The secret used to verify incoming GitHub webhook signatures, ensuring authenticity.
*   `OPENAI_BASE_URL` (Optional): The base URL for the OpenAI API (defaults to `https://api.openai.com/v1`).
*   `DEFAULT_MODEL_NAME` (Optional): The OpenAI model to use for description generation (defaults to `gpt-4-turbo-preview`).
*   `PORT` (Optional): The port on which the bot's web server will listen (defaults to `8000`).