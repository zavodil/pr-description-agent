import os
import httpx
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class OpenAIClient:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.base_url = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
        self.model = os.getenv('DEFAULT_MODEL_NAME', 'gpt-4-turbo-preview')

    async def generate_description(self, diff_content: str, pr_title: str) -> Optional[str]:
        """Generate PR description based on diff content"""
        prompt = self._create_prompt(diff_content, pr_title)

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        data = {
            'model': self.model,
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 1000,
            'temperature': 0.3
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f'{self.base_url}/chat/completions',
                    headers=headers,
                    json=data,
                    timeout=60.0
                )

                if response.status_code == 200:
                    return response.json()['choices'][0]['message']['content']
                else:
                    print(f"OpenAI API error: {response.status_code}")
                    return None

            except Exception as e:
                print(f"OpenAI request failed: {e}")
                return None

    def _create_prompt(self, diff_content: str, pr_title: str) -> str:
        """Create prompt for OpenAI"""
        return f"""
Analyze this git diff and create a clear, professional PR description.

PR Title: {pr_title}

Git Diff:
{diff_content}

Generate a description that includes:
- **What changed** (bullet points of main changes)
- **Why** (reason for these changes)
- **Technical details** (important implementation notes)

Keep it concise, professional, and under 500 words.
Use markdown formatting for better readability.
"""