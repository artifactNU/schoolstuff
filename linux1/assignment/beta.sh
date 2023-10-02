#!/bin/bash
MY_INPUT='userinfo.csv'

#while read -r line; do
#    echo "$line"
#done <"$MY_INPUT"

while IFS="," read -r firstname surname password operation; do
    #om användaren redan finns
    if id -u "$firstname$surname" >/dev/null 2>&1; then
        echo "användaren $firstname$surname existerar redan"
        exit 1
    fi
    echo "$operation" -m "$firstname$surname" -p "$password"
done < <(sed 1d "$MY_INPUT")
