#!/usr/bin/env python3

joltage = 0

with open("input.txt") as f:
    for line in f:
        l = list(map(int, list(line.strip())))
        m = 0
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                ll = zip(l[i:], l[j:])
                m = max(m, max([x * 10 + y for x, y in ll]))
        joltage += m

print(joltage)
