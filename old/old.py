import os
import sys
import json
import requests

# Authentication for user filing issue
USERNAME = 'VanGutan' # change this to own username
PASSWORD = 'token' # change this to own token

# The repository to add this issue to
REPO_OWNER = 'ringwormGO-organization'
repo_name = None

def make_github_issue(title, body=None):
    #Create an issue on github.com using the given parameters.
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, repo_name)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body
    }
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print(f"Successfully created issue {format(title)}")
    else:
        print(f"Could not create Issue {format(title)}")
        print("Response:", r.content)


if __name__ == "__main__":
    if sys.argv[1] == "-h":
        print("<repo name> <title> <body>")

    repo_name = sys.argv[1]
    make_github_issue(sys.argv[2], sys.argv[3])
