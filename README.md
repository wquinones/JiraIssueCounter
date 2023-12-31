# Jira Issue Counter

Jira Issue Counter is a Python-based tool that provides monthly counts of Jira tickets reported by specified users across multiple projects. It works with the Jira REST API, enabling users to retrieve and analyze ticket data from their projects based on provided parameters.

## Features

- Track tickets that are opened, closed, or both.
- Ability to fetch data between specific date ranges.
- Results can be printed on the console or saved in a CSV file.
- Reporters can be specified to narrow down the statistics.
- Multiple projects can be specified for combined analysis.
- The script can be tailored for specific Jira subdomains and projects.

## Requirements

- Python 3.6 or higher
- Python libraries: `requests`, `pandas`, `prettytable`, `dateutil`, `argparse`, `os`, `base64`

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/wquinones/JiraIssueCounter.git
    ```
2. Navigate to the cloned repository:
    ```bash
    cd JiraIssueCounter
    ```
3. Install the required Python libraries:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

To use the script, you will need to provide several command-line arguments. For example:

```bash
python JiraIssueCounter.py --startdate 2023-01-01 --enddate 2023-06-30 --jirasubdomain myjira --reporters "user1","user2","user3" --project myproject --searchtype all --output console --email myatlassianemail@example.com
```
Here is a breakdown of the arguments:

Here is a breakdown of the arguments:

- `-s` / `--startdate`: The start date for the range of tickets to consider (YYYY-MM-DD).
- `-e` / `--enddate`: The end date for the range of tickets to consider (YYYY-MM-DD).
- `-u` / `--jirasubdomain`: Your Jira subdomain.
- `-a` / `--reporters`: A comma-separated list of Jira reporters to consider.
- `-p` / `--project`: A comma-separated list of project names to consider.
- `-t` / `--searchtype`: The type of tickets to consider (options: `opened`, `closed`, `all`).
- `-o` / `--output`: The type of output (options: `console`, `csv`).
- `-m` / `--email`: The email to use for Jira authentication.


## Authentication

This script uses basic authentication with your Jira API token. Make sure you have your Jira API token saved as an environment variable named `JIRA_API_TOKEN` before running the script.

## License

This project is licensed under the terms of the MIT license.
