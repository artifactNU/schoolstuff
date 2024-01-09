#!/bin/bash

#find . -name "*sh" | while IFS= read -r file; do
#  ls -l "$file"
#done

for i in $(find . -type f -name "*sh"); do
  ls -l "$i"
done