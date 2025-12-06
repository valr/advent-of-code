#!/usr/bin/env python3

with open("input1.txt") as f:
    op = f.readline().split()

total = [0 if o == "+" else 1 for o in op]

with open("input2.txt") as f:
    for line in f:
        for i, num in enumerate(map(int, line.strip().split())):
            total[i] = total[i] + num if op[i] == "+" else total[i] * num

print(sum(total))
