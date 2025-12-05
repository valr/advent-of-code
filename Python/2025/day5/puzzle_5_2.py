#!/usr/bin/env python3

ranges = []

with open("input1.txt") as f:
    for line in f:
        ranges.append(list(map(int, line.strip().split("-"))))

ranges = sorted(ranges, key=lambda x: x[0])

# The below code has been adapted a bit. However the original working version
# has been automatically provided by copilot under vscode without any user prompt!
# It probably means copilot has pumped all the code from other AoC participants.
for i in range(1, len(ranges)):
    if ranges[i][0] <= ranges[i - 1][1]:
        ranges[i - 1][1] = max(ranges[i - 1][1], ranges[i][1])
        ranges[i - 1], ranges[i] = [-1, -1], ranges[i - 1]

print(sum([j - i + 1 for i, j in ranges if i != -1]))
