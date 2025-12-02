#!/usr/bin/env python3


def is_valid_id(id: int) -> bool:
    s = str(id)
    sz = len(s)
    return s[0 : sz // 2] == s[sz // 2 :]


sum = 0

with open("input.txt") as file:
    line = file.readline()

for range_ in line.split(","):
    start, stop = map(int, range_.split("-"))
    for id in range(start, stop + 1):
        if is_valid_id(id):
            sum += id

print(sum)
