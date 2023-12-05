#!/usr/bin/env python3

import re
import sys

with open("puzzle_5.txt") as file:
    lines = file.read().splitlines()

seeds = [int(n) for n in lines[0].split()[1:]]

maps = "\n".join(lines[1:]).split("\n\n")
maps = [[int(n.group(0)) for n in re.finditer(r"\d+", m)] for m in maps]

lowest_location = sys.maxsize
for seed in seeds:
    location = seed
    for map_ix in range(len(maps)):
        for rng_ix in range(0, len(maps[map_ix]), 3):
            dst, src, rng = maps[map_ix][rng_ix : rng_ix + 3]
            if location >= src and location < src + rng:
                location = dst - src + location
                break
    lowest_location = min(lowest_location, location)
print(f"lowest location: {lowest_location}")
