#!/usr/bin/env python3

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


build_map('puzzle_3_1.txt', 100)
trees = traverse_map(3, 1)

print(f'number of trees: {trees}')
