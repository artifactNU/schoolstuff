#!/bin/bash

# Krav:
# 1. Skriptet tar endast ett argument, en CSV-fil.
# 2. CSV-filen innehåller fyra kolumner: firstname, surname, password, operation.
# 3. Operationskolumnen innehåller antingen add eller remove.
# 4. Paketet whois måste vara installerat. sudo apt install whois
# 5. Skriptet måste köras med root-rättigheter.
# 6. Loggfilen ligger/skapas i samma katalog som skriptet.

if test $# -ne 1; then                             # kontrollera att endast ett argument har angets & att det är en fil som existerar
    echo "ange endast en csv-fil som argument" >&2 # error print till stderr
    exit 1
fi

MY_INPUT="$1"           # user info csv-fil
LOGG_FILE='logfile.txt' # definiera loggfil

touch "$LOGG_FILE" # skapa loggfil om den inte finns

if test ! -f "$MY_INPUT"; then                         # kontrollera att argumentet är en vanlig fil
    echo "argumentet består inte av en vanlig fil" >&2 # error print till stderr
    exit 1
fi

while IFS="," read -r firstname surname password operation; do # IFS="," gör csv-filen läsbar
    username="${firstname:0:3}${surname:0:3}"                  # definiera användarnamn & ta hänsyn på namn < 3 bokstäver
    if test "$operation" = "add"; then                         # kolla om användare ska skapas
        if id -u "$username" 2>/dev/null; then                 # kolla om användaren finns, output discarded
            echo "användaren $username existerar redan" >&2    # error print till stderr
        fi
        echo "Skapar användare: $username" | tee -a "$LOGG_FILE"        #BONUS# logga skapande
        useradd -m "$username" -p "$(mkpasswd "$password")" 2>/dev/null #BONUS# skapa användare med hashat lösenord & home directory
        echo "Genererar hash för $username" >&2                        #BONUS#
    elif test "$operation" = "remove"; then                             #BONUS# kolla om användare ska raderas
        if ! id -u "$username" 2>/dev/null; then                        #BONUS# kolla om användaren inte finns, output discarded
            echo "användaren $username existerar inte" >&2              #BONUS# error print til stderr
        fi
        echo "Raderar användare: $username" | tee -a "$LOGG_FILE" #BONSU# logga radering
        userdel -r "$username" 2>/dev/null                        #BONUS# radera användare & home directory, output discarded
    else
        echo "okänt kommando: $operation använd add/remove" >&2 # error print till stderr
        exit 1
    fi
done <"$MY_INPUT"
