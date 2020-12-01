#!/usr/bin/env python3

with open('puzzle_1_1.txt') as file:
    numbers = [int(line) for line in file]

for n1 in numbers:
    for n2 in numbers:
        if n1+n2 == 2020:
            print(f'n1: {n1}, n2: {n2}, n1*n2: {n1*n2}')
