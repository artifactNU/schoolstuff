#!/bin/bash

if [ "$(systemctl is-active apache2)" == "active" ]; then
    echo "Apache2 is running $(date)" >>/var/log/apache2/apache2cronjob.log
else
    echo "Apache2 is not running $(date)" >>/var/log/apache2/apache2cronjob.log
fi
