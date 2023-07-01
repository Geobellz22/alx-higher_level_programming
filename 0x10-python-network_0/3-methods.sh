#!/bin/bash
# Bash script that takes in a UR and display HTTPS methods
curl -siLX OPTIONS "$1" | grep "Allow" | awk -F ': ' ' {print $2}'
