#!/bin/bash

result=0
while read line; do
  result=$(( result + line ))
done < "puzzle1a.txt"
echo $result
