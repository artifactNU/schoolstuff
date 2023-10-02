#!/bin/bash

#seq 1 30>nummer #lägg nr1-30 i filen number

#pipe |

#kommandon
# sort -g               - sortera i nummerisk följd
# uniq                  - filtrera dubbletter
# tee <filnamn>         - dirigerar om stdout till <filnamn> och skriver ut stdin till stdout
# cut

# cat namn.txt | cut -d ',' -f 1,3

cat nummer | sort -g | uniq | tee skript_pipes_nummer
