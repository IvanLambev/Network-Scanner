#!/bin/bash

for ip in 192.168.1.{1..255}; do
    ping -c 1 $ip > /dev/null
    if [ $? -eq 0 ]; then
        echo "Host $ip is up"
        # Call the Python script to extract information about the device
        python3 network_scanner.py $ip
    fi
done
