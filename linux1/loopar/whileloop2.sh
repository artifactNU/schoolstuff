#!/bin/bash

# reader-ternary.sh

while read -r x; do
    echo "Du skrev: $x"
    test "$x" = "quit" && echo "Hej då!" && exit 0 # ["$x" = "quit"] && echo "Hej då!" && exit 0
    sleep 1
done
