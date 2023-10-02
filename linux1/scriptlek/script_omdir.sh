#!/bin/bash

#dirigerar om stdout till en fil
echo works >skript_omdir_stdout

# 1 stdout - skriptets primära syfte
# 2 stderr - errors, diagnostik etc
# 0 stdin - ostast tangentbordet

#dirigera om stdout till stderr
echo Felmeddelande >&2

#dirigerar om båda sätt#1
echo Felmeddelande >skript_omdir_allt 2>skript_omdir_allt
#2
echo Felmeddelande >skript_omdir_allt 2>&1
