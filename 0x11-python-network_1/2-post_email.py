#!/usr/python3
""" python script that takes in a URL and an email,
sends email sends a post request"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    value = urllib.parse.urlencode(data).encode("ascii")

    req = urllib.request.Request(sys.argv[1], value)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8")
