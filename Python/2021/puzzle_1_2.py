#!/usr/bin/env python3

with open("puzzle_1_2.txt") as file:
    depths = [int(line) for line in file]

depths = [d1 + d2 + d3 for d1, d2, d3 in zip(depths, depths[1:], depths[2:])]

# same as for puzzle 1
n = len([d for d in zip(depths, depths[1:]) if d[0] < d[1]])
print(f"number of times a depth measurement increases: {n}")
