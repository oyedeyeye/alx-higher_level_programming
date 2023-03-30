#!/usr/bin/bash
# script that takes in a URL, sends a request to that URL, and displays
curl -sI "$1" | grep 'Content-Length:' | cut -d ' ' -f2
