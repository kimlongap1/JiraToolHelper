import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import os
from dotenv import load_dotenv
 
 # Load environment variables from .env file
load_dotenv()
# Retrieve credentials from environment variables
email = os.getenv('JIRA_EMAIL')
api_token = os.getenv('JIRA_API_TOKEN')
domain = os.getenv('JIRA_DOMAIN')
project_key = "LS"
 
# Define headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Load data from the Excel sheet
excel_file = 'jira_issues_with_epic_details.xlsx'  # Replace with your Excel file name
df = pd.read_excel(excel_file)

# Step 1: Create the EPIC
epic_payload = {
    "fields": {
        "project": {
            "key": project_key
        },
        "summary": df.loc[0, 'EPIC Summary'],  # Assuming EPIC summary is in the first row and named 'EPIC Summary'
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "heading",
                    "attrs": {
                        "level": 2
                    },
                    "content": [
                        {
                            "text": "Issue/Things Need to Solve (WHAT)",
                            "type": "text"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": df.loc[0, 'EPIC Description'],  # Assuming EPIC description is in the first row and named 'EPIC Description'
                            "type": "text"
                        }
                    ]
                },
                {
                    "type": "heading",
                    "attrs": {
                        "level": 2
                    },
                    "content": [
                        {
                            "text": "Purpose/Objective (WHY)",
                            "type": "text"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": df.loc[0, 'EPIC Purpose/Objective'],  # Assuming this is in a column named 'EPIC Purpose/Objective'
                            "type": "text"
                        }
                    ]
                },
                {
                    "type": "heading",
                    "attrs": {
                        "level": 2
                    },
                    "content": [
                        {
                            "text": "Suggested Approaches and Solutions",
                            "type": "text"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": df.loc[0, 'EPIC Suggested Approaches'],  # Assuming this is in a column named 'EPIC Suggested Approaches'
                            "type": "text"
                        }
                    ]
                },
                {
                    "type": "heading",
                    "attrs": {
                        "level": 2
                    },
                    "content": [
                        {
                            "text": "Outcome Expectations",
                            "type": "text"
                        }
                    ]
                },
                {
                    "type": "bulletList",
                    "content": [
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "text": f"Customer perspective: {df.loc[0, 'EPIC Customer Outcome']}",  # Assuming this is in a column named 'EPIC Customer Outcome'
                                            "type": "text"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "text": f"System performance perspective: {df.loc[0, 'EPIC System Outcome']}",  # Assuming this is in a column named 'EPIC System Outcome'
                                            "type": "text"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "text": f"Security perspective: {df.loc[0, 'EPIC Security Outcome']}",  # Assuming this is in a column named 'EPIC Security Outcome'
                                            "type": "text"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "heading",
                    "attrs": {
                        "level": 2
                    },
                    "content": [
                        {
                            "text": "Resource Estimation (SWAG)",
                            "type": "text"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": df.loc[0, 'EPIC Resource Estimation'],  # Assuming this is in a column named 'EPIC Resource Estimation'
                            "type": "text"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Epic"
        }
    }
}

# Make the request to create the EPIC
epic_response = requests.post(
    f"https://{domain}/rest/api/3/issue",
    data=json.dumps(epic_payload),
    headers=headers,
    auth=HTTPBasicAuth(email, api_token)
)

if epic_response.status_code == 201:
    epic_key = epic_response.json()['key']
    print(f"Created EPIC: {epic_key}")
else:
    print(f"Failed to create EPIC: {epic_response.status_code}, {epic_response.text}")
    exit()

# Step 2: Create User Stories linked to the EPIC using the Epic Link
for i in range(0, len(df)):
    story_payload = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": df.loc[i, 'Story Summary'],  # Assuming Story summary is in a column named 'Story Summary'
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": df.loc[i, 'Story Description'],  # Assuming Story description is in a column named 'Story Description'
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "type": "heading",
                        "attrs": {
                            "level": 2
                        },
                        "content": [
                            {
                                "text": "Acceptance Criteria",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "type": "bulletList",
                        "content": [
                            {
                                "type": "listItem",
                                "content": [
                                    {
                                        "type": "paragraph",
                                        "content": [
                                            {
                                                "text": df.loc[i, 'Acceptance Criteria'],  # Assuming Acceptance Criteria is in a column named 'Acceptance Criteria'
                                                "type": "text"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "heading",
                        "attrs": {
                            "level": 2
                        },
                        "content": [
                            {
                                "text": "Definition of Done (DoD)",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "type": "bulletList",
                        "content": [
                            {
                                "type": "listItem",
                                "content": [
                                    {
                                        "type": "paragraph",
                                        "content": [
                                            {
                                                "text": df.loc[i, 'Definition of Done (DoD)'],  # Assuming DoD is in a column named 'Definition of Done (DoD)'
                                                "type": "text"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Story"
            },
            "parent": {
                "key": epic_key  # This ensures the story is created as a child of the EPIC
            }
        }
    }

    # Make the request to create the User Story
    story_response = requests.post(
        f"https://{domain}/rest/api/3/issue",
        data=json.dumps(story_payload),
        headers=headers,
        auth=HTTPBasicAuth(email, api_token)
    )

    if story_response.status_code == 201:
        story_key = story_response.json()['key']
        print(f"Created User Story: {story_key}")
    else:
        print(f"Failed to create User Story: {story_response.status_code}, {story_response.text}")