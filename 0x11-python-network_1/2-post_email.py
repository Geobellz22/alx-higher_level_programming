#!/usr/bin/python3
""" Python script that takes in a URL
and an email sends a post request
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as res:
        body = response.read().decode('utf-8')
    print(body)
