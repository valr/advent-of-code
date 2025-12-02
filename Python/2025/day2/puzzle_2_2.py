#!/usr/bin/env python3


def is_valid_id(id: int) -> bool:
    # string periodicity test using doubling
    s = str(id)
    sz = len(s)
    if sz < 2:
        return False
    i = (s + s).find(s, 1)
    return i > 0 and i < sz


sum = 0

with open("input.txt") as file:
    line = file.readline()

for range_ in line.split(","):
    start, stop = map(int, range_.split("-"))
    for id in range(start, stop + 1):
        if is_valid_id(id):
            sum += id

print(sum)
