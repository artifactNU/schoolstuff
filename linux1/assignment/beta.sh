#!/bin/bash
MY_INPUT='userinfo.csv'
LOGG_FILE='logfile.txt'

#while read -r line; do
#    echo "$line"
#done <"$MY_INPUT"

while IFS="," read -r firstname surname password operation; do # IFS="," gör csv filen läsbar
    # om användaren redan finns
    if id -u "$firstname$surname" >/dev/null 2>&1; then
        echo "användaren $firstname$surname existerar redan" >&2
        exit 1
    fi
    # skapa användaren med lösenordet - ta bort echo
    echo "$operation" -m "$firstname$surname" -p "$password"
    # skippa första raden i csv-filen
done < <(sed 1d "$MY_INPUT")
