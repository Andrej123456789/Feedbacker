import os
from os.path import exists
import sys
import time
import json
import requests

# Authentication for user filing issue
USERNAME = 'VanGutan' # change this to own username
PASSWORD = '' # change this to own token

# The repository to add this issue to
REPO_OWNER = 'ringwormGO-organization'
repo_name = None

def get_operating_system() -> str:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if sys.platform == "win32": 
        return "Windows"
    else:
        return "GNU/Linux"

def help():
    print("<repo name> <title> <body>")
    exit(0)

def write_time():
    if exists(".time.txt"):
        os.remove(".time.txt")

    if get_operating_system() == "Windows":
        f = open(".time.txt", "a+")
        os.system("attrib +h .time.txt")
    else:
        f = open(".time.txt", "a+")
    f.write(str(time.time()))

def check_time() -> int:
    if exists(".time.txt"):
        write_time()
        f = open(".time.txt", "r")
        tmp_time = float(f.read())
        if tmp_time + 600 == tmp_time:
            return 0
        else:
            print("You need to wait 10 minutes from the last issue")
            return 1
    else:
        print("Can't check time, writing from this moment!")
        return 2

def return_time() -> float:
    if exists(".time.txt"):
        f = open(".time.txt", "r")
        return float(f.read())
    else:
        print("Writing time...")
        write_time()
        f = open(".time.txt", "r")
        return float(f.read())

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
        write_time()
    else:
        print(f"Could not create issue {format(title)}")
        print("Response:", r.content)


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        help()

    if sys.argv[1] == "-h":
        help()

    if check_time() != 1:
        repo_name = sys.argv[1]
        make_github_issue(sys.argv[2], sys.argv[3])