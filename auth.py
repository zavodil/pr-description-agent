import os
import time
import jwt
import httpx
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class GitHubAuth:
    def __init__(self):
        self.app_id = os.getenv('GITHUB_APP_ID')
        self.private_key = self._load_private_key()

    def _load_private_key(self) -> str:
        """Load GitHub App private key"""
        private_key_path = os.getenv('GITHUB_PRIVATE_KEY_PATH')
        private_key_content = os.getenv('GITHUB_PRIVATE_KEY')

        if private_key_path and os.path.exists(private_key_path):
            with open(private_key_path, 'r') as f:
                return f.read()
        elif private_key_content:
            # Handle multiline private key from env var
            return private_key_content.replace('\\n', '\n')
        else:
            raise ValueError("GitHub private key not found")

    def generate_jwt_token(self) -> str:
        """Generate JWT token for GitHub App authentication"""
        now = int(time.time())
        payload = {
            'iat': now,
            'exp': now + 600,  # 10 minutes
            'iss': self.app_id
        }

        return jwt.encode(payload, self.private_key, algorithm='RS256')

    async def get_installation_token(self, installation_id: int) -> Optional[str]:
        """Get installation access token"""
        jwt_token = self.generate_jwt_token()

        headers = {
            'Authorization': f'Bearer {jwt_token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        url = f'https://api.github.com/app/installations/{installation_id}/access_tokens'

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, timeout=30.0)

                if response.status_code == 201:
                    return response.json()['token']
                else:
                    print(f"Failed to get installation token: {response.status_code}")
                    return None

            except Exception as e:
                print(f"Error getting installation token: {e}")
                return None