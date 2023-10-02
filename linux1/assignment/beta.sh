#!/bin/bash
MY_INPUT='userinfo.csv'

while read -r line; do
    echo "$line"
done <"$MY_INPUT"

while IFS="," read -r firstname surname password operation; do
    echo "$operation" -m "$firstname$surname" -p "$password"
done <"$MY_INPUT"
