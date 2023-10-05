#!/bin/bash

# brace {}

echo {a,b}              #=> echo a b
cp fil{,.backup}        #=> cp fil fil.backup
cp fil{,.backup{1..10}} #=> S/A men 10 nummrerade backup
