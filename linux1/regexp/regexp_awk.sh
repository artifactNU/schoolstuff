#!/bin/bash
# while true; do clear ; ./regexp_awk.sh namn.txt; sleep 2 ; done

#hela raden är $0
#awk awk '{ print $0}' <"$1"

#awk '/bob/ { print $0}' <"$1"

#awk 'END { print $ND}' <"$1"

#skriv ut kolumn x
#awk '{ print $2 }' "$1"

#awk '/fish$/ { print $2 }' "$1"

awk '/\/sh$/ { print $2 * 2 }' "$1"
