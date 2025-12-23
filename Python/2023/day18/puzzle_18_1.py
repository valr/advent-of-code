#!/usr/bin/env python3

import numpy as np
import scipy as sp

grid = np.zeros((1000, 1000), dtype=int)

with open("puzzle_18.txt") as file:
    lines = file.read().splitlines()

posy, posx = 500, 500
grid[posy, posx] = 1

for line in lines:
    direction, length, _ = [int(i) if i.isnumeric() else i for i in line.split()]

    while length:
        if direction == "R":
            posx += 1
        elif direction == "L":
            posx -= 1
        elif direction == "D":
            posy += 1
        elif direction == "U":
            posy -= 1

        if posy < 0 or posx < 0:
            raise ValueError("can't handle negative values")

        grid[posy, posx] = 1
        length -= 1  # type: ignore

filled_grid = sp.ndimage.binary_fill_holes(grid).astype(int)
print(np.unique(filled_grid, return_counts=True))  # use count of 1
