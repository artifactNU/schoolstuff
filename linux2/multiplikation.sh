#!/bin/bash

# Loop from 1 to 10
for i in {1..10}; do
  for j in {1..10}; do
    # Print the multiplication result
    echo "$i * $j = $((i*j))"
  done
  # Newline for readability
  echo ""
done