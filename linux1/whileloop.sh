#!/bin/bash

# while kör medans uttrycket är sant

while test -e runjustrun; do
    echo "Filen finns ännu!"
    sleep 1
done

echo "Filen finns inte längre!"
