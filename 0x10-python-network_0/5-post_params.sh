#!/bin/bash
# Bash script that takes in a URL, send a post request to the passed URL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"