#!/usr/bin/env python3
from itertools import chain


def irange(start, stop):
    return range(start, stop + 1)


with open("puzzle_5_1.txt") as file:
    lines = file.read().splitlines()
    coords = [[int(n) for n in line.replace(" -> ", ",").split(",")] for line in lines]
    coords = [c for c in coords if c[0] == c[2] or c[1] == c[3]]

max_ = max(chain(*coords)) + 1
# diagram = max_ * [[0] * max_]   ook ook!
diagram = [[0] * max_ for m in range(max_)]

for coord in coords:
    if coord[0] == coord[2]:
        for y in irange(*sorted([coord[1], coord[3]])):
            diagram[y][coord[0]] += 1
    else:
        for x in irange(*sorted([coord[0], coord[2]])):
            diagram[coord[1]][x] += 1

overlap = len([point for point in list(chain(*diagram)) if point >= 2])
print(f"At how many points do at least two lines overlap: {overlap}")
