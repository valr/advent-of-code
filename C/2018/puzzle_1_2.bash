#!/bin/bash

# hahaha lol, this is super ugly!

declare -a array

result=1000000
array[$result]="present"

while true; do
  while read line; do
    result=$((result + line))
    if [ "${array[$result]}" = "present" ]; then
      echo $((result - 1000000))
      exit 0
    fi
    array[$result]="present"
  done <"puzzle1b.txt"
done
