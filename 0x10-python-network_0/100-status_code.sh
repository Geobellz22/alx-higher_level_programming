#!/bin/bash
# Bash script that sends request a URL passed as an argument
curl -s -o /dev/null -w "%{http_code}" "$1"
