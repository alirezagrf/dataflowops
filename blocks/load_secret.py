import requests
import json
import os,subprocess

def get_secrets(repo_name):

    # Set up the authentication for the Github API
    auth_token = os.getenv('GITHUB_TOKEN')
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    # Call the Github API to get the list of secrets for the repository
    secrets_url = f"https://api.github.com/repos/alirezagrf/{repo_name}/actions/secrets"
    secrets_response = requests.get(secrets_url, headers=headers)
    secrets_data = json.loads(secrets_response.text)
    sec = []
    for secret in secrets_data['secrets']:
        sec.append(secret['name'])
    return sec

if __name__ == "__main__":

    secrets = get_secrets('dataflowops')
    for secret in secrets:
        command_s = f'"{secret}=$' + "{{" + f"secrets.{secret}" + '}}" >> $GITHUB_ENV'
        # print(command_s)
        # os.system(command_s)
        subprocess.call(['call',command_s], shell=True)
        # print(f"{secret} added to ENV")
    