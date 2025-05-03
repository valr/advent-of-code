#!/usr/bin/env python3
from itertools import chain

with open("puzzle_4_1.txt") as file:
    lines = file.read().splitlines()

num = [int(n) for n in lines[0].split(",")]
num_bingo = int((len(lines) - 1) / 6)
bingo = [[int(n) for n in line.split()] for line in lines[1:] if line]


def bingooo(n):
    for nb in range(num_bingo):
        for y in range(5):
            for x in range(5):
                if bingo[nb * 5 + y][x] == n:
                    bingo[nb * 5 + y][x] = None


def first_winner():
    list_nb, list_n = [], []
    for n in num:
        bingooo(n)
        for nb in range(num_bingo):
            for y in range(5):
                if not any(bingo[nb * 5 + y]):
                    if nb not in list_nb:
                        list_nb.append(nb)
                        list_n.append(n)

            for x in range(5):
                if not any([b[x] for b in bingo[nb * 5 : nb * 5 + 5]]):
                    if nb not in list_nb:
                        list_nb.append(nb)
                        list_n.append(n)

        if len(list_nb) == 1:
            return list_n[-1], list_nb[-1]


n, nb = first_winner()
score = sum([r for r in list(chain(*bingo[nb * 5 : nb * 5 + 5])) if r is not None]) * n
print(f"Final score: {score}")
