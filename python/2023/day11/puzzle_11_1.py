#!/usr/bin/env python3

from itertools import combinations

import numpy as np


def expand_image(image):
    new_image = []
    for i in image:
        new_image.append(i)
        if i.count(".") == len(i):
            new_image.append(i)
    return new_image


with open("puzzle_11.txt") as file:
    image = file.read().splitlines()

image = expand_image(image)
image = ["".join(j) for j in np.rot90([list(i) for i in image], 3)]
image = expand_image(image)
image = ["".join(j) for j in np.rot90([list(i) for i in image], 1)]

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
    sum_steps += abs(y1 - y2) + abs(x1 - x2)

print(f"sum of steps: {sum_steps}")
