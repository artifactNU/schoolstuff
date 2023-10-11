#!/bin/bash
# add to crontab -e : * * * * * sh /path/to/grupparb.sh

loggfil=/home/administrator/schoolstuff/linux1/assignment/loggfil.txt

log() {
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    echo "$TIMESTAMP" "$@" >>$loggfil
}
log "backup start"

log "backup finished"
