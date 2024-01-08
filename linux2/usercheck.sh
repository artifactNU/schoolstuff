#!/bin/bash

user=$1

grep "$user" /etc/passwd
grep "$user" /etc/group