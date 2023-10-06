#!/bin/bash

LOGGFIL="$1"

cat "$LOGGFIL" | grep -E 'Oct[ ]+06[ ]+' | grep -E '[pid [0-9]]*' | grep -E 'AH00163'
