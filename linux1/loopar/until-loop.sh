#!/bin/bash

# until kör tills uttrycket är sant

until test -e runjustrun; do
    echo "Vi kör ännu"
    sleep 1
done

echo "Filen finns!"
