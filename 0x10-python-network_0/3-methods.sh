#!/bin/bash
#Bash script that takes in a URL and displays all HTP method
curl -sI "$1" | grep "ALLOW": | cut -f2- -d' '
