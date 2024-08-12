#!/usr/bin/env python3

from itertools import combinations

from numpy import rot90

with open("puzzle_11.txt") as file:
    image = file.read().splitlines()

yexpands = [row_ix for row_ix, row in enumerate(image) if row.count(".") == len(row)]
image = ["".join(j) for j in rot90([list(i) for i in image], 3)]
xexpands = [row_ix for row_ix, row in enumerate(image) if row.count(".") == len(row)]
image = ["".join(j) for j in rot90([list(i) for i in image], 1)]

galaxies = [
    (y, x)
    for y in range(len(image))
    for x in range(len(image[y]))
    if image[y][x] != "."
]

pairs = list(combinations(galaxies, 2))

sum_steps = 0

for pair in pairs:
    (y1, x1), (y2, x2) = pair
    y1, y2 = sorted([y1, y2])
    x1, x2 = sorted([x1, x2])

    yexp = [1000000 for y in yexpands if y > y1 and y < y2]
    xexp = [1000000 for x in xexpands if x > x1 and x < x2]

    sum_steps = (
        sum_steps
        + (y2 - y1)
        + (x2 - x1)
        - len(yexp)
        + sum(yexp)
        - len(xexp)
        + sum(xexp)
    )

print(f"sum of steps: {sum_steps}")
