#!/bin/bash
# Bash script that takes in a url, send request to the url
curl -s "$1" | wc -c
