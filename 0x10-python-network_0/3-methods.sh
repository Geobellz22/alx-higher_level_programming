#!/bin/bash
#Bash script that takes in a URL and displays all HTP method
curl -sL "$1" | grep "ALLOW" |  cut -d " " -f 2-
