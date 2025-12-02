#!/usr/bin/env python3


# # original version (poor performance)
# def is_valid_id(id):
#     s = str(id)
#     sz = len(s)
#     for n in range(1, sz // 2 + 1):
#         l = [s[i : i + n] for i in range(0, sz, n)]
#         if len(set(l)) <= 1:
#             return True
#     return False


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
