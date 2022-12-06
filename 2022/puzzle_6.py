#!/usr/bin/env python3

from collections import Counter

with open("puzzle_6.txt") as file:
    line = file.read().strip()

# s = 4
s = 14
for i in range(0, len(line)):
    if max(Counter(line[i : i + s]).values()) == 1:
        print(i + s)
        break
