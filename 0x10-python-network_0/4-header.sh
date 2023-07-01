#!/bin/bash
# Bash script that takes in a URL as an argument, send a GET request to the URl
curl -sH "X-School-User-Id: 98" "${1}"
