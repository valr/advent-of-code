#!/usr/bin/env python3


def count_split(diag, row, col):
    global count
    for r in range(row, len(diag)):
        if diag[r][col] == "^":
            if diag[r][col - 1 : col + 2] != "|^|":
                count += 1
            if diag[r][col - 1] != "|":
                count_split(diag, r, col - 1)
            if diag[r][col + 1] != "|":
                count_split(diag, r, col + 1)
            break
        else:
            diag[r] = diag[r][:col] + "|" + diag[r][col + 1 :]


with open("input.txt") as f:
    diag = f.read().splitlines()

count = 0
count_split(diag, 0, diag[0].find("S"))
print(count)
