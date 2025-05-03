#!/usr/bin/env python3

import numpy as np

with open("puzzle_14.txt") as file:
    lines = file.read().splitlines()
    lines = ["".join(j) for j in np.rot90([list(i) for i in lines], 3)]  # not strictly necessary, but well

for line_ix, line in enumerate(lines):
    line_ln = len(line)

    i = line_ln - 1
    while i >= 0:
        if lines[line_ix][i] == "O":
            j = i + 1
            while j < line_ln and lines[line_ix][j] == ".":
                j += 1
            j = j - 1
            if j > i and j < line_ln and lines[line_ix][j] == ".":
                lines[line_ix] = lines[line_ix][:i] + "." + lines[line_ix][i + 1 :]
                lines[line_ix] = lines[line_ix][:j] + "O" + lines[line_ix][j + 1 :]
        i -= 1

total_load = 0

for line in lines:
    total_load += sum([char_ix + 1 for char_ix, char in enumerate(line) if char == "O"])

print(f"total load on the north support beams: {total_load}")
