import requests
from requests.auth import HTTPBasicAuth

 # Load environment variables from .env file
load_dotenv()
# Retrieve credentials from environment variables
email = os.getenv('JIRA_EMAIL')
api_token = os.getenv('JIRA_API_TOKEN')
domain = os.getenv('JIRA_DOMAIN')
# List of issue keys you want to delete
issue_keys = ["LS-692","LS-693","LS-694","LS-695","LS-696"]  # Replace with the actual issue keys

# Function to delete an issue
def delete_issue(issue_key):
    url = f"https://{domain}/rest/api/3/issue/{issue_key}"
    
    response = requests.delete(
        url,
        auth=HTTPBasicAuth(email, api_token)
    )
    
    if response.status_code == 204:
        print(f"Issue {issue_key} deleted successfully.")
    elif response.status_code == 404:
        print(f"Issue {issue_key} not found, skipping.")
    else:
        print(f"Failed to delete issue {issue_key}: {response.status_code}, {response.text}")

# Loop through each issue key and attempt to delete it
for issue_key in issue_keys:
    delete_issue(issue_key)