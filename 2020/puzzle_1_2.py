#!/usr/bin/env python3

from itertools import combinations
from math import prod

with open('puzzle_1_2.txt') as file:
    numbers = [int(line) for line in file]


def original_solution():
    # super ugly, of course
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n1+n2+n3 == 2020:
                    print(f'n1: {n1}, n2: {n2}, n3: {n3}, n1*n2*n3: {n1*n2*n3}')


def reworked_solution(r):
    # less ugly, still inneficient
    return prod([n for n in combinations(numbers, r) if sum(n) == 2020][0])


print("original solution:")
original_solution()

print("reworked solution:")
print(reworked_solution(3))
