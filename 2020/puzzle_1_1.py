#!/usr/bin/env python3

numbers = []
with open('puzzle_1_2.txt') as file:
    for line in file:
        numbers.append(int(line))

# lazy solution
for n1 in numbers:
    for n2 in numbers:
        if n1+n2 == 2020:
            print(f'n1: {n1}, n2: {n2}, n1*n2: {n1*n2}')
