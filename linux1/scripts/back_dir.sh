#!/bin/bash

# verifiera att ett argument har angetts
if test -z "$1" ; then                                                              # test -z testar om en sträng är tom
    echo "Saknar argument. Ange en katalog för att skapa en säkerhetskopia." >&2
    exit 1
fi

# verifiera att argumentet är en existerande katalog
if test ! -d "$1"; then                                                             # test -d testar om det är en katalog
    echo "Argumentet är inte en existerande katalog." >&2
    exit 1
fi

# om en backup med namnet $1.bak redan finns, döp om den till $1.bak2
# gammal $1.bak2 raderas
if test -e "$1.bak"; then                                                           # test -e testar om den existerar
    if test -e "$1.bak2"; then 
        rm -r "$1.bak2"                                                             # rm -r tar bort en katalog och dess innehåll
    fi
    mv "$1.bak" "$1.bak2"
fi

# skapa en säkerhetskopia av katalogen $1
# varje filnamn skrivs ut under tiden de kopieras
cp -rv "$1" "$1.bak" | while read -r line; do                     # -rv kopierar rekursivt och skriver ut filnamn |  while read -r line = läs in varje rad i $line
    echo "$line"
done
