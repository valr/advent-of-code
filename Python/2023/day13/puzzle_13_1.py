#!/usr/bin/env python3

import numpy as np


def reflection(lines):
    refl = []

    for line_ix in range(len(lines) - 1):
        if lines[line_ix] == lines[line_ix + 1]:
            match, match_ix1, match_ix2 = True, line_ix, line_ix + 1
            while match_ix1 >= 0 and match_ix2 < len(lines):
                if lines[match_ix1] != lines[match_ix2]:
                    match = False
                    break

                match_ix1 -= 1
                match_ix2 += 1

            if match:
                refl.append(line_ix + 1)

    return refl


with open("puzzle_13.txt") as file:
    patterns = file.read().split("\n\n")

result = 0

for pattern in patterns:
    lines = pattern.split()
    result += sum([r * 100 for r in reflection(lines)])

    lines = ["".join(j) for j in np.rot90([list(i) for i in lines], 3)]
    result += sum(reflection(lines))

print(f"result: {result}")
