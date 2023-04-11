#!/bin/bash
#Bash script that takes in a URL and Display the size in bytes
curl -s "$1" | wc -c
