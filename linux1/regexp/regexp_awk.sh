#!/bin/bash
# while true; do clear ; ./regexp_awk.sh namn.txt; sleep 2 ; done

#hela raden är $0
#awk awk '{ print $0}' <"$1"

#awk '/otta/ { print $0}' <"$1"

awk 'END { print $ND}' <"$1"
