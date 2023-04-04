#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display
the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
"""


import sys
import requests

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv[1]) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    data = {"q": letter}

    req = requests.post(url, data=data)

    try:
        res = req.json()
        if res:
            print("[{}] {}".format(res.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
