#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with email as a parameter, displays body of response
The email must be sent in the email variable
"""


import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}
    req = requests.post(url, data=payload)
    print(req.text)
