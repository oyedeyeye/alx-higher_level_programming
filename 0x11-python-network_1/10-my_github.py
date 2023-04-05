#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id. Use Basic Authentication with a
personal access token as password to access your information (only read:user
permission is needed). first argument will be your username, second argument
will be your password (in your case, a personal access token as password)
"""


import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    basic = HTTPBasicAuth(username, password)

    url = 'https://api.github.com/user'

    req = requests.get(url, auth=basic)

    if bool(req) is not False:
        result = req.json()
        print(result['id'])
    else:
        print("None")
