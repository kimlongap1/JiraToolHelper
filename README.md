
# Jira Automation Script

## Introduction

This project contains a Python script that automates the creation of Jira EPICs and User Stories based on data provided in an Excel file. The script uses the Jira REST API to create issues, and it relies on environment variables for credentials and configuration. The project follows best practices by storing sensitive information, such as API tokens and email addresses, in a `.env` file, which is excluded from the repository using `.gitignore`.

## Features

- Create Jira EPICs with detailed descriptions, including issues to solve, objectives, suggested approaches, and outcome expectations.
- Automatically generate and link User Stories to the EPIC.
- Securely manage credentials using environment variables.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Jira account with the necessary permissions to create issues.
- Jira API token and domain information.

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your `.env` file**:
    Create a `.env` file in the root directory of the project with the following contents:

    ```plaintext
    JIRA_EMAIL=your_email@example.com
    JIRA_API_TOKEN=your_api_token
    JIRA_DOMAIN=your_domain.atlassian.net
    ```

### How to Get Jira Token and Domain

#### Jira API Token

1. **Log in to your Jira account**.
2. **Go to [Atlassian API Token Management](https://id.atlassian.com/manage-profile/security/api-tokens)**.
3. **Click on "Create API token"**.
4. **Give your token a label/name** and click **Create**.
5. **Copy the token** and paste it into your `.env` file as `JIRA_API_TOKEN`.

#### Jira Domain

Your Jira domain is typically in the format `your-domain.atlassian.net`. You can find it in your Jira project URL:

For example, if your Jira project URL is `https://mycompany.atlassian.net/jira/software/projects/MYPROJ/boards/1`, then your domain is `mycompany.atlassian.net`.

Add this domain to your `.env` file as `JIRA_DOMAIN`.

### Running the Script

After setting up your environment and credentials, you can run the script to create Jira EPICs and User Stories:

```bash
python your_script_name.py
