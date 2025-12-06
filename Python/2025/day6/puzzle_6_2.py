#!/usr/bin/env python3

import numpy as np

with open("input1.txt") as f:
    op = f.readline()

p = op.find(" ")
while p != -1:
    op = op.replace(" ", op[p - 1], 1)
    p = op.find(" ")
op = op[::-1]

num = []
with open("input2.txt") as f:
    for line in f:
        num.append(list(line.strip("\n")))
num = np.rot90(num)

total = []
for i, n in enumerate(num):
    s = "".join(n).strip()
    if not s:
        total.append(0 if op[i] == "+" else 1)
    else:
        if not total:
            total.append(0 if op[i] == "+" else 1)
        total[-1] = total[-1] + int(s) if op[i] == "+" else total[-1] * int(s)
print(sum(total))
