#!/bin/bash
#Raderar filer som är äldre än <days> dagar.
directory="/path/to/directory"
days=1
find "$directory" -type f -mtime +$days -exec rm {} \;
