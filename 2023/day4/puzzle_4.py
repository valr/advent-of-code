#!/usr/bin/env python3

import re

with open("puzzle_4.txt") as file:
    lines = file.read().splitlines()

total_points = 0
total_scratchcards = [1] * len(lines)
for index, line in enumerate(lines):
    card = re.split(r":|\|", line)
    win = set([n.group(0) for n in re.finditer(r"\d+", card[1])]) & set(
        [n.group(0) for n in re.finditer(r"\d+", card[2])]
    )
    if win:
        total_points += 2 ** (len(win) - 1)

        for i in range(total_scratchcards[index]):
            for j in range(len(win)):
                total_scratchcards[index + j + 1] += 1

print(f"total_points: {total_points}")
print(f"total_scratchcards: {sum(total_scratchcards)}")
