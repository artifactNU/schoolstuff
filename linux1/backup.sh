#!/bin/bash
backup_dir="/path/to/backup"
source_file="/path/to/source/file"
backup_file="backup_$(date +%Y%m%d%H%M%S).txt"
cp "$source_file" "$backup_dir/$backup_file"
