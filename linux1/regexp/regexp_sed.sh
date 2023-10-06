#!/bin/bash

sed -E 's/ +\././g' <fil.txt | sed -E 's/\./.\n/g' | sed -E 's/  +/ /g' | sed -E 's/^(-.+)\.$/B\1E/g'
