#!/usr/bin/python3
""" send a request to the URL
and displays the value of X-Request-Id"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(sys.argv[1]) as res:
        headers = res.getheaders()
        for i in headers:
            if i[0] == 'X-Request-Id':
                print(i[1])
