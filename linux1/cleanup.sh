#!/bin/bash
directory="/path/to/directory"
days=7
find "$directory" -type f -mtime +$days -exec rm {} \;
