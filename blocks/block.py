import requests
import json
from prefect.blocks.system import Secret
import os

def get_secret_value(repo_name, secret_name):
    # Set up the authentication for the Github API
    auth_token = os.getenv('GITHUB_TOKEN')
    headers = {"Authorization": f"Token {auth_token}"}
    
    # Call the Github API to get the list of secrets for the repository
    secrets_url = f"https://api.github.com/repos/{repo_name}/actions/secrets"
    secrets_response = requests.get(secrets_url, headers=headers)
    secrets_data = json.loads(secrets_response.text)
    
    # Search for the secret with the given name
    for secret in secrets_data["secrets"]:
        if secret["name"] == secret_name:
            # Call the Github API to get the value of the secret
            secret_url = secret["url"]
            secret_response = requests.get(secret_url, headers=headers)
            secret_data = json.loads(secret_response.text)
            return secret_data["data"]["value"]
    
    # If the secret is not found, return None
    return None


if __name__ == "__main__":
    Secret(value=get_secret_value('dataflowops','MY_SECRET')).save(name='my-secret',overwrite=True)