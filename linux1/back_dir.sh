#!/bin/bash

# verifiera att ett argument har angetts.
if test "$1" -eq 0; then
    echo "Saknar argument. Ange en katalog för att skapa en säkerhetskopia." >&2
    exit 1
fi

# verifiera att argumentet är en existerande katalog.
if test ! -d "$1"; then
    echo "Argumentet är inte en existerande katalog." >&2
    exit 1
fi

# om en backup med namnet $1.bak redan finns, döp om den till $1.bak2. Befintlig $1.bak2 raderas om den existerar innan omdöpningen.
if test -e "$1.bak"; then
    if test -e "$1.bak2"; then
        rm "$1.bak2"
    fi
    mv "$1.bak" "$1.bak2"
fi

# skapa en säkerhetskopia av katalogen $1. Varje filnamn skrivs ut under tiden de kopieras
cp -r "$1" "$1.bak" | while read -r line; do
    echo "$line"
done
