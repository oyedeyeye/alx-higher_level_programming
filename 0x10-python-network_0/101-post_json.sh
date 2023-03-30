#!/bin/bash
# sends JSON POST request passed as first argument, displays body of response
curl -sL -H "Content-Type:application/json" -d @"$2" -X POST "$1"
