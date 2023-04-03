#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with email as a parameter, displays body of response (decoded in utf-8)
The email must be sent in the email variable
"""


import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        body_content = res.read()
        print(body_content.decode("utf-8"))
