#!/bin/bash

# Loop from 1 to 10
for i in {1..10}; do
    # Nested 1 to 10
  for j in {1..10}; do
    # Print result
    echo "$i * $j = $((i*j))"
    if test $i == $j
    then
        echo "hej"
    fi
  done
  # Newline
  echo ""
done