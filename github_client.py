import httpx
from typing import Optional


class GitHubClient:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    async def get_pr_info(self, owner: str, repo: str, pr_number: int) -> Optional[dict]:
        """Get PR basic information"""
        url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}'

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=self.headers, timeout=30.0)

                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Failed to get PR info: {response.status_code}")
                    return None

            except Exception as e:
                print(f"Error getting PR info: {e}")
                return None

    async def get_pr_diff(self, owner: str, repo: str, pr_number: int) -> Optional[str]:
        """Get PR diff content"""
        url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}'
        diff_headers = {
            **self.headers,
            'Accept': 'application/vnd.github.v3.diff'
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=diff_headers, timeout=30.0)

                if response.status_code == 200:
                    return response.text
                else:
                    print(f"Failed to get PR diff: {response.status_code}")
                    return None

            except Exception as e:
                print(f"Error getting PR diff: {e}")
                return None

    async def update_pr_description(self, owner: str, repo: str, pr_number: int, description: str) -> bool:
        """Update PR description"""
        url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}'
        data = {'body': description}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.patch(url, headers=self.headers, json=data, timeout=30.0)

                if response.status_code == 200:
                    return True
                else:
                    print(f"Failed to update PR: {response.status_code}")
                    return False

            except Exception as e:
                print(f"Error updating PR: {e}")
                return False