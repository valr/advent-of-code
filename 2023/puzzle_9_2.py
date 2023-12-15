#!/usr/bin/env python3

with open("puzzle_9.txt") as file:
    hists = [list(map(int, line.split())) for line in file.read().splitlines()]

sum_extrapolation = 0

for hist in hists:
    diffs = [hist]
    while any(diffs[-1]):
        diffs.append(
            [
                diffs[-1][diff_ix + 1] - diffs[-1][diff_ix]
                for diff_ix in range(len(diffs[-1]) - 1)
            ]
        )

    extrapolation = 0
    for diff_ix in range(len(diffs) - 1, -1, -1):
        extrapolation = diffs[diff_ix][0] - extrapolation
    sum_extrapolation += extrapolation

print(f"sum of extrapolated values: {sum_extrapolation}")
