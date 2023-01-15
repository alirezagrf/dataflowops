# import requests
# import json
# from prefect.blocks.system import Secret
import os,sys

def get_secret_value(repo_name, secret_name):
    # Set up the authentication for the Github API
    # auth_token = os.getenv('GITHUB_TOKEN')
    auth_token = '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'

    headers = {"Authorization": f"Bearer {auth_token}"}
    
    # Call the Github API to get the list of secrets for the repository
    secrets_url = f"https://api.github.com/repos/alirezagrf/{repo_name}/actions/secrets/{secret_name}"
    secrets_response = requests.get(secrets_url, headers=headers)
    secrets_data = json.loads(secrets_response.text)
    print(secrets_data)


if __name__ == "__main__":
    # Secret(value=get_secret_value('dataflowops','MY_SECRET')).save(name='my-secret',overwrite=True)
    print(sys.argv['Object'])
    # print(get_secret_value('dataflowops','MY_SECRET'))