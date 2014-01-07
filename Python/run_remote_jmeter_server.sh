#!/bin/bash
# My first script
# "jeep" "audi" "honda" 
servers=("audi")


for host in "${servers[@]}"
do
	echo "Connecting to $host"
	ssh $host 'bash -s' < commands.sh
done