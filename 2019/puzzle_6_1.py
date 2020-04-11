#!/usr/bin/env python3

def count_orbit(obj):
    y = [x for x in orbit if obj in orbit[x]]
    if y:
        return count_orbit(y[0]) + 1
    else:
        return 0

orbit = {}

with open('puzzle_6_1.input') as file:
    for line in file:
        x, y = line.strip().split(')')
        if x not in orbit:
            orbit[x] = []
        orbit[x].append(y)

print(sum([sum([count_orbit(x) for x in orbit[y]]) for y in orbit]))
