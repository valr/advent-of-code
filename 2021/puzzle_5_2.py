#!/usr/bin/env python3
from itertools import chain


def irange(start, stop, step=1):
    return range(start, stop + (1 if step > 0 else -1), step)


with open("puzzle_5_2.txt") as file:
    lines = file.read().splitlines()
    coords = [[int(n) for n in line.replace(" -> ", ",").split(",")] for line in lines]

max_ = max(chain(*coords)) + 1
diagram = [[0] * max_ for m in range(max_)]

for coord in coords:
    if coord[0] == coord[2]:
        for y in irange(*sorted([coord[1], coord[3]])):
            diagram[y][coord[0]] += 1
    elif coord[1] == coord[3]:
        for x in irange(*sorted([coord[0], coord[2]])):
            diagram[coord[1]][x] += 1
    else:
        x = coord[0]
        for y in irange(coord[1], coord[3], 1 if coord[1] <= coord[3] else -1):
            diagram[y][x] += 1
            x += 1 if coord[0] <= coord[2] else -1

overlap = len([point for point in list(chain(*diagram)) if point >= 2])
print(f"At how many points do at least two lines overlap: {overlap}")
