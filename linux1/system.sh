#!/bin/bash
echo "System Information"
echo "------------------"
echo "Hostname: $(hostname)"
echo "CPU: $(lscpu | grep 'Model name' | awk -F ': ' '{print $2}')"
echo "Memory: $(free -h | awk '/^Mem/ {print $2}')"
