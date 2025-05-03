#!/usr/bin/env python3

from itertools import accumulate, chain

def make_step(move):
    step = {'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0)}
    for loop in range(int(move[1:])):
        yield step[move[0]]

def make_path(line):
    path = [(0,0)]
    for step in map(make_step, line.split(',')):
        path = chain(path, step)
    return list(accumulate(path, lambda s1, s2: (s1[0]+s2[0], s1[1]+s2[1])))

f = open('puzzle_3_1.input')
path1 = make_path(f.readline())
path2 = make_path(f.readline())

distance = sorted([abs(p[0])+abs(p[1]) for p in path1 if p in path2])

print("Manhattan distance:", distance[1])
