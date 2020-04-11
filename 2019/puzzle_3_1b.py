#!/usr/bin/env python3

from itertools import accumulate
from shapely.geometry import LineString

def parse(d):
    direction = {
        'U': (lambda x: (0,-x)),
        'D': (lambda x: (0, x)),
        'L': (lambda x: (-x,0)),
        'R': (lambda x: ( x,0))}
    return direction[d[0]](int(d[1:]))

def wire(l):
    line = 'U0,' + l
    return list(accumulate(
           list(map(parse, line.split(','))),
           lambda p1, p2: (p1[0]+p2[0], p1[1]+p2[1])))

f = open('puzzle_3_1.input')
wire1 = wire(f.readline())
wire2 = wire(f.readline())

distance = []
for index1 in range(len(wire1)-1):
    for index2 in range(len(wire2)-1):
        line1 = LineString(wire1[index1:index1+2])
        line2 = LineString(wire2[index2:index2+2])
        intersection = line1.intersection(line2)
        if intersection.bounds:
            distance.append(int(abs(intersection.bounds[0]) +
                                abs(intersection.bounds[1])))

print(min(d for d in distance if d > 0))
