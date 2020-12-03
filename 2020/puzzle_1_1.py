#!/usr/bin/env python3

from itertools import combinations
from math import prod

with open('puzzle_1_1.txt') as file:
    numbers = [int(line) for line in file]


def original_solution():
    # super ugly, of course
    for n1 in numbers:
        for n2 in numbers:
            if n1+n2 == 2020:
                print(f'n1: {n1}, n2: {n2}, n1*n2: {n1*n2}')


def reworked_solution(r):
    # less ugly, still inneficient
    return prod([n for n in combinations(numbers, r) if sum(n) == 2020][0])


print("original solution:")
original_solution()

print("reworked solution:")
print(reworked_solution(2))
