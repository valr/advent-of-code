#!/usr/bin/env python3

ranges = []
with open("input1.txt") as f:
    for line in f:
        ranges.append(list(map(int, line.strip().split("-"))))

count = 0
with open("input2.txt") as f:
    for line in f:
        i = int(line.strip())
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                count += 1
                break
print(count)
