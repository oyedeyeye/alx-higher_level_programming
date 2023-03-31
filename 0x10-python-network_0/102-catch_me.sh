#!/bin/bash
# makes a request that causes the server to respond with specific message
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "You got me!"
