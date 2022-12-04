#!/usr/bin/env python3

import re

with open("puzzle_4.txt") as file:
    lines = file.read().splitlines()

count1, count2 = 0, 0
for line in lines:
    i1, i2, i3, i4 = map(int, re.split(",|-", line))
    s1, s2 = set(range(i1, i2 + 1)), set(range(i3, i4 + 1))
    ov = s1.intersection(s2)
    if len(ov) == len(s1) or len(ov) == len(s2):
        count1 += 1
    if ov:
        count2 += 1
print(count1)
print(count2)
