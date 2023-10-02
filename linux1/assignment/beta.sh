#!/bin/bash
MY_INPUT='userinfo.csv'
LOGG_FILE='logfile.txt'

while IFS="," read -r firstname surname password operation; do                          # IFS="," gör csv-filen läsbar
    if test "$operation" = "add"; then                                                  # kolla om användare ska skapas
        if id -u "$firstname$surname" >/dev/null; then                                  # kolla om användaren finns, output discarded
            echo "användaren $firstname$surname existerar redan" >&2                    # error print till stderr
            exit 1
        fi
        echo "$operation" -m "$firstname$surname" -p "$password" | tee -a "$LOGG_FILE"  # skapa användare och logga utan att skriva över
    elif test "$operation" = "remove"; then                                             # kolla om användare ska raderas
        if ! id -u "$firstname$surname" >/dev/null; then                                # kolla om användaren finns, output discarded
            echo "användaren $firstname$surname existerar inte" >&2                     # error print til stderr
            exit 1
        fi
        userdel -r "$firstname$surname" | tee -a "$LOGG_FILE"                           # radera användare och logga utan att skriva över
    else
        echo "okänt kommando: $operation använd add/remove" >&2
        exit 1
    fi
done < <(sed 1d "$MY_INPUT")                                                            # ignorera header i csv-filen