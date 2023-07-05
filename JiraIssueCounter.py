import os
import requests
import pandas as pd
from prettytable import PrettyTable
from argparse import ArgumentParser
from dateutil.rrule import rrule, MONTHLY
from datetime import datetime
from dateutil.relativedelta import relativedelta
import base64


def get_args():
    parser = ArgumentParser(description="Get count of Jira tickets by users")
    parser.add_argument("-s", "--startdate", required=True, help="Start date")
    parser.add_argument("-e", "--enddate", required=True, help="End date")
    parser.add_argument("-u", "--jirasubdomain", required=True, help="Jira subdomain")
    parser.add_argument("-a", "--assignees", required=True, help="Assignee names, comma-separated")
    parser.add_argument("-p", "--project", required=True, help="Project name")
    parser.add_argument("-t", "--searchtype", required=True, help="Search type: opened, closed, all")
    parser.add_argument("-o", "--output", default="console", help="Output type: console, csv")
    parser.add_argument("-m", "--email", required=True, help="User email for authentication")
    return parser.parse_args()

def get_monthly_counts(args):
    api_token = os.getenv('JIRA_API_TOKEN')
    email = args.email
    startdate = datetime.strptime(args.startdate, '%Y-%m-%d')
    enddate = datetime.strptime(args.enddate, '%Y-%m-%d')
    base_url = f"https://{args.jirasubdomain}.atlassian.net/rest/api/2/search"
    assignees = args.assignees.split(',')
    searchtype = args.searchtype
    output_type = args.output
    project = args.project
    dates = [dt for dt in rrule(MONTHLY, dtstart=startdate, until=enddate)]
    
    if searchtype == 'opened':
        table = PrettyTable()
        table.field_names = ["User"] + [f'{date.strftime("%B")} Opened' for date in dates]
    elif searchtype == 'closed':
        table = PrettyTable()
        table.field_names = ["User"] + [f'{date.strftime("%B")} Closed' for date in dates]
    else:
        table = PrettyTable()
        table.field_names = ["User"] + [item for date in dates for item in [f'{date.strftime("%B")} Opened', f'{date.strftime("%B")} Closed']]

    data = []

    headers = {
       "Accept": "application/json",
       "Authorization": f"Basic {base64.b64encode(f'{email}:{api_token}'.encode()).decode()}"
    }

    for assignee in assignees:
        row = [assignee]
        for date in dates:
            jql_opened = f'project={project} AND assignee="{assignee}" AND created>={date.strftime("%Y-%m-%d")} AND created<{(date+relativedelta(months=+1)).strftime("%Y-%m-%d")}'
            jql_closed = f'project={project} AND assignee="{assignee}" AND resolved>={date.strftime("%Y-%m-%d")} AND resolved<{(date+relativedelta(months=+1)).strftime("%Y-%m-%d")}'
            if searchtype in ['all', 'opened']:
                row.append(get_ticket_count(jql_opened, headers, base_url))
            if searchtype in ['all', 'closed']:
                row.append(get_ticket_count(jql_closed, headers, base_url))
        data.append(row)

    for row in data:
        table.add_row(row)

    if output_type == 'console':
        print(table)
    elif output_type == 'csv':
        df = pd.DataFrame(data, columns=table.field_names)
        filename = f"{args.startdate}-{args.enddate}-{args.searchtype}.csv"
        df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")

def get_ticket_count(jql, headers, base_url):
    query = {'jql': jql}
    response = requests.get(base_url, headers=headers, params=query)
    data = response.json()
    return data['total']

if __name__ == "__main__":
    args = get_args()
    get_monthly_counts(args)
