#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""


import sys
import urllib.request


if __name__ == '__main__':

    try:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            content = res.read()
            print(content.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
