#!/usr/bin/env python3

with open("puzzle_6.txt") as file:
    line = file.read().strip()

# s = 4
s = 14
for i in range(len(line)):
    if len(set(line[i : i + s])) == s:
        print(i + s)
        break
