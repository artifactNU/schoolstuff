#!/bin/bash

# parameter expansion, bra om man vill ändra på strängar

VAR="Myrslok"
VAR2=${1:-Fallback} # ange ett argument

# enklaste
echo OUT 1: "$VAR"
echo OUT 2: "$VAR2"

# del
echo OUT 3: "${VAR:0:3}" # tre första tecken
echo OUT 4: "${VAR:3}"   # tecken efter tre första
echo OUT 5: "${#VAR}"    # strängläng
echo OUT 6: "${M##VAR}"  # ta bort prefix
#P="/etc/hej/"
#echo OUT 7: "${/%%P}"    # ta bort sufix
#echo OUT 8: "${VAR/Myr/Hund}"
