#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
using the package urllib
"""


import requests

if __name__ == '__main__':

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res.text))
    print("\t- utf8 content: {}".format((res.decode('utf-8'))))
