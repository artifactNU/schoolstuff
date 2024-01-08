#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "No argument provided. Please provide a username."
  exit 1
fi

user=$1

grep "$user" /etc/passwd
grep "$user" /etc/group