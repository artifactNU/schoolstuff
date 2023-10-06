#!/bin/bash

VAR=something

# i annan fil som vill använda func.sh
# source /home/administrator/schoolstuff/linux1/functions/func.sh

function prefix_three {
    echo 1: "$1" "$VAR"
}

function prefix_three {
    echo 1 ${1:0:3}
    EXIT=0
    return $EXIT
}
