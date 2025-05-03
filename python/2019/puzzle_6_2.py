#!/usr/bin/env python3

def list_orbit(obj):
    y = [x for x in orbit if obj in orbit[x]]
    if y:
        return list_orbit(y[0]) + y
    else:
        return []

orbit = {}

with open('puzzle_6_2.input') as file:
    for line in file:
        x, y = line.strip().split(')')
        if x not in orbit:
            orbit[x] = []
        orbit[x].append(y)

print(len(set(list_orbit('YOU')) ^ set(list_orbit('SAN'))))
