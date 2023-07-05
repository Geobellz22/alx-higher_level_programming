#!/usr/bin/python3
"""Python script that takes in a URL
and displays the body of the response
"""
import sys
import urllib.sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.open(req) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
