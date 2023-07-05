# Jira Issue Counter

Jira Issue Counter is a Python-based tool that provides monthly counts of Jira tickets for specified users across multiple projects. It works with the Jira REST API, enabling users to retrieve and analyze ticket data from their projects based on provided parameters.

## Features

- Track tickets that are opened, closed, or both.
- Ability to fetch data between specific date ranges.
- Results can be printed on the console or saved in a CSV file.
- Users can be specified to narrow down the statistics.
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
python jira_ticket_analyzer.py --startdate 2023-01-01 --enddate 2023-06-30 --jirasubdomain myjira --assignees "user1","user2","user3" --projects "myproject1,myproject2" --searchtype all --output console --email myatlassianemail@example.com

Here is a breakdown of the arguments:

- `-s` / `--startdate`: The start date for the range of tickets to consider (YYYY-MM-DD).
- `-e` / `--enddate`: The end date for the range of tickets to consider (YYYY-MM-DD).
- `-u` / `--jirasubdomain`: Your Jira subdomain.
- `-a` / `--assignees`: A comma-separated list of Jira usernames to consider.
- `-p` / `--projects`: A comma-separated list of project names to consider.
- `-t` / `--searchtype`: The type of tickets to consider (options: `opened`, `closed`, `all`).
- `-o` / `--output`: The type of output (options: `console`, `csv`).
- `-m` / `--email`: The email to use for Jira authentication.

## Authentication

This script uses basic authentication with your Jira API token. Make sure you have your Jira API token saved as an environment variable named `JIRA_API_TOKEN` before running the script.

## Contributing

We welcome contributions to the Jira Ticket Analyzer. Please open an issue or submit a pull request if you would like to contribute.

## License

This project is licensed under the terms of the MIT license.

