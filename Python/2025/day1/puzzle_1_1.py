#!/usr/bin/env python3

count = 0

with open("input.txt") as f:
    position = 50
    for line in f:
        direction, step = 1 if line[0] == "R" else -1, int(line[1:])
        position += direction * step
        if position % 100 == 0:
            count += 1

print(count)
