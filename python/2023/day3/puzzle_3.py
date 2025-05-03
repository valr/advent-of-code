#!/usr/bin/env python3

import math
import re

with open("puzzle_3.txt") as file:
    lines = file.read().splitlines()

engine = [[char for char in line] for line in lines]

sum_adjacent_symbol = 0
num_adjacent_stars = []
for y in range(0, len(engine)):
    y1 = y - 1 if y > 0 else y
    y2 = y + 1 if y + 1 < len(engine) else y
    for num in re.finditer(r"\d+", "".join(engine[y])):
        x1 = num.start() - 1 if num.start() > 0 else num.start()
        x2 = num.end() - 1 if num.end() >= len(engine[y]) else num.end()
        n = int("".join(engine[y][num.start() : num.end()]))

        adjacent = False
        for y3 in range(y1, y2 + 1):
            part = engine[y3][x1 : x2 + 1]

            # number adjacent to a symbol
            if set(part) - set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]):
                adjacent = True

            # number adjacent to a star
            if "*" in part:
                num_adjacent_stars.append((y1, y2, x1, x2, n))

        if adjacent:
            sum_adjacent_symbol += n

print(f"sum_adjacent_symbol: {sum_adjacent_symbol}")

sum_gear_ratio = 0
for y in range(0, len(engine)):
    for x in range(0, len(engine[y])):
        # star symbol...
        if engine[y][x] == "*":
            gear = []

            # ...adjacent to...
            for i in range(0, len(num_adjacent_stars)):
                y1, y2, x1, x2, n = num_adjacent_stars[i]
                if y >= y1 and y <= y2 and x >= x1 and x <= x2:
                    gear.append(n)

            # ...exactly two part numbers
            if len(gear) == 2:
                sum_gear_ratio += math.prod(gear)

print(f"sum_gear_ratio: {sum_gear_ratio}")
