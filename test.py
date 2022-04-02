import os
import sys
import time
import json
import requests

# Authentication for account designed to create issue (must have read/write access to repository to add issue to)
USERNAME = "VanGutan"
TOKEN = "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"

# The repository to add this issue to
REPO_OWNER = "ringwormGO-organization"
repo_name = None

title = None
body = None
assignee = 'username'
closed = False
labels = [
    
]

def make_github_issue():
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = f"https://api.github.com/repos/{REPO_OWNER}/{repo_name}/import/issues"
    
    # Headers
    headers = {
        f"Authorization": "token {TOKEN}",
        "Accept": "application/vnd.github.golden-comet-preview+json"
    }
    
    # Create our issue
    data = {'issue': {'title': title,
                      'body': body,
                      'assignee': assignee,
                      'closed': closed,
                      'labels': labels}}

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", url, data = payload, headers = headers)
    if response.status_code == 202:
        print(f"Successfully created issue {title}")
    else:
        print(f"Could not create issue! {title}")
        print(f"Response: {response.content}")



if __name__ == "__main__":
    last_created = open("last.txt", "a")

    if not int(last_created) + 600 >= int(last_created):
        print("Can't create new issue, you need wait 10 minutes from last minute.")
    else:
        try:
            if sys.argv[1] or sys.argv[2] or sys.argv[3] or sys.argv[4] or sys.argv[5] == None:
                print("There is no enough arguments or it is wrong! Exiting...")
                exit(0)
        except Exception as error:
            print(error)
            print("Exiting... ")
            exit(0)

        repo_name = sys.argv[1]
        title = sys.argv[2]
        body = open(sys.argv[3], "r")
        assignee = sys.argv[4]
        labels.append(sys.argv[5])
        try:
            labels.append(sys.argv[6])
            make_github_issue()
        except:
            print(f"Can't add more labels to {labels}")
            make_github_issue()

        last_created.write(time.time())