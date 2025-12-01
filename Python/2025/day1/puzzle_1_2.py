#!/usr/bin/env python3


def count_cross_zero(count, position, direction, step):
    for _ in range(step):
        position += direction
        if position % 100 == 0:
            count += 1
    return count, position


count = 0

with open("input.txt") as f:
    position = 50
    for line in f:
        direction, step = 1 if line[0] == "R" else -1, int(line[1:])
        count, position = count_cross_zero(count, position, direction, step)

print(count)
