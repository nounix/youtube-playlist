#!/bin/bash

# Get name of all files
# find . -type f -printf "%f\n" | sed -e 's/\.[^\.]*$//' | sed -e 's,_, ,g' > ~/list.txt

FAILCOUNT=0

while IFS='' read -r line || [[ -n "$line" ]]; do
    YTID="$(wget -q -O- "https://www.youtube.com/results?search_query=$line" | grep -m1 -oP 'href="\/watch\?v=\K.{11}')"
    [[ -z "$YTID" ]] && ((FAILCOUNT++)) || FAILCOUNT=0
    [[ "FAILCOUNT" -gt 5 ]] && echo "Use diff vpn" && exit
	echo "$YTID" >> id.list
done < "$1"
