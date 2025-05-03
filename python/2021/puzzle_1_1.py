#!/usr/bin/env python3

with open("puzzle_1_1.txt") as file:
    depths = [int(line) for line in file]

n = len([d for d in zip(depths, depths[1:]) if d[0] < d[1]])
print(f"number of times a depth measurement increases: {n}")
