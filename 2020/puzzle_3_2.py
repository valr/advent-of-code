#!/usr/bin/env python3

from math import prod

map = []


def build_map(filename, repetition):
    global map

    with open(filename) as file:
        map = [line.strip() * repetition for line in file]


def traverse_map(x, y):
    global map

    posx, count = 0, 0
    for posy in range(0, len(map), y):
        if map[posy][posx] == '#':
            count += 1
        posx += x

    return count


build_map('puzzle_3_2.txt', 100)
trees = [traverse_map(x, y) for x, y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]

print(f'number of trees: {prod(trees)}')
