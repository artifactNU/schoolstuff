#!/bin/bash

# Definiera funktionen för att kontrollera om ett gränssnitt är uppe
check_interface() {
    if ping -I $1 -c 1 8.8.8.8 &>/dev/null; then
        echo "$(date): $1 is up" >>networklog.txt
    else
        echo "$(date): $1 is down" >>networklog.txt
    fi
}

# Kontrollera gränssnitten
check_interface eno1
check_interface wlan0
