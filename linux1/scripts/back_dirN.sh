#!/bin/bash

# validera att minst ett argument har angivits
if test $# -lt 1; then                                                                 # $# = antal argument  -lt = less than
    echo "Saknar argument. Ange minst en katalog för att skapa en säkerhetskopia." >&2
    exit 1
fi

# loopa igenom alla angivna argument och verifiera att de är existerande kataloger
for dir in "$@"; do                                                                    # $@ = alla argument
    if test ! -d "$dir"; then                                                          # ! -d = inte en katalog
        echo "Argumentet '$dir' är inte en existerande katalog." >&2
        exit 1
    fi
done

# loopa igenom alla angivna argument och skapa en backup för varje katalog
for dir in "$@"; do
    # om en backup med namnet $#.bak redan finns, döp om den till $#.bak2
    # radera befintlig $#.bak2 om den existerar innan omdöpningen
    if test -e "$dir.bak"; then                                                        # -e = existerar
        if test -e "$dir.bak2"; then
            rm -r "$dir.bak2"                                                          # -r = rekursivt
        fi
        mv "$dir.bak" "$dir.bak2"
    fi

    # skapa en ny backup av katalogen och namnge den till $#.bak
    # varje filnamn skrivs ut medans de kopieras
    cp -rv "$dir" "$dir.bak" | while read -r line; do                                  # -rv = rekursivt och verbose | while read -r line = läs in varje rad i $line
        echo "$line"
    done
done