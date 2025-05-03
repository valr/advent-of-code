#!/usr/bin/env python3

with open("puzzle_1.txt") as file:
    lines = file.read().splitlines()

calories = [0]
for line in lines:
    if line:
        calories[-1] += int(line)
    else:
        calories.append(0)

print(max(calories))
print(sum(sorted(calories)[-3:]))
