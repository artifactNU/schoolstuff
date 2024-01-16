#!/bin/bash

# MySQL user configuration
username="username"
password="password"
database="database"

# File configuration
backup_path="/path/to/your/backup/directory"
date=$(date +"%d-%b-%Y")

# Create a backup
mysqldump --user=$username --password=$password --databases $database >$backup_path/$database-$date.sql
