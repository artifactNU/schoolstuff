#!/bin/bash

#går igenom alla argument
# $1 $2 .. $#
for arg; do
    test -d "$arg" && rmdir "$arg"
    echo "argument: $arg"
done

echo "slut"
