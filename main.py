import os
import sys
import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'VanGutan'
PASSWORD = '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'

# The repository to add this issue to
REPO_OWNER = 'ringwormGO-organization'
REPO_NAME = 'Croatix'

def make_github_issue(title, body=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
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
        print('Successfully created issue {0:s}'.format(title))
    else:
        print('Could not create Issue {0:s}'.format(title))
        print('Response:', r.content)


if __name__ == "__main__":
    if sys.argv[1] == "-h":
        print("<title> <body>")

    make_github_issue(sys.argv[1], sys.argv[2])