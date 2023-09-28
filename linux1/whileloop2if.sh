#!/bin/bash

while read -r x; do
    echo "Du skrev: $x"

    if [ "$x" = "quit" ]; then
        echo "Hej då"
        exit 0
    fi

    sleep 1
done
