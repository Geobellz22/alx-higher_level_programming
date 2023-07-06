#!/usr/bin/python3
""" Python script that takes in a URL
and an email, sends a POST request"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = {"emai": sys.argv[2]}
    value = urllib.parse.urlencode(data).encode("ascii")

    req = urllib.request.Request(sys.argv[1], value)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
