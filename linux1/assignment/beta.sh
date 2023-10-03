#!/bin/bash

if test $# -ne 1; then                                   # kontrollera att endast ett argument har angets & att det är en fil som existerar
    echo "ange endast exakt en csv-fil som argument" >&2 # error print till stderr
    exit 1
fi

MY_INPUT="$1" # user info csv-fil
LOGG_FILE='logfile.txt'

if test ! "$1" -f; then # kontrollera att argumentet är en vanlig fil
    echo "argumentet består inte av en vanlig fil" >&2 # error print till stderr
    exit 1
fi

while IFS="," read -r firstname surname password operation; do       # IFS="," gör csv-filen läsbar
    username="${firstname:0:3}${surname:0:3}"                        # definiera användarnamn
    if test "$operation" = "add"; then                               # kolla om användare ska skapas
        if id -u "$username" >/dev/null; then               # kolla om användaren finns, output discarded
            echo "användaren $username existerar redan" >&2 # error print till stderr
            exit 1
        fi
        # ta bort echo
        echo useradd -m "$username" -p "$password" | tee -a "$LOGG_FILE" # skapa användare och logga utan att skriva över
    elif test "$operation" = "remove"; then                              # kolla om användare ska raderas
        if ! id -u "$username" >/dev/null; then                          # kolla om användaren inte finns, output discarded
            echo "användaren $username existerar inte" >&2               # error print til stderr
            exit 1
        fi
        # ta bort echo
        echo userdel -r "$username" | tee -a "$LOGG_FILE" # radera användare och logga utan att skriva över
    else
        echo "okänt kommando: $operation använd add/remove" >&2 # error print till stderr
        exit 1
    fi
done < <(sed 1d "$MY_INPUT") # ignorera header i csv-filen