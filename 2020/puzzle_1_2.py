#!/usr/bin/env python3

numbers = []
with open('puzzle_1_1.txt') as file:
    for line in file:
        numbers.append(int(line))

# lazy solution
for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if n1+n2+n3 == 2020:
                print(f'n1: {n1}, n2: {n2}, n3: {n3}, n1*n2*n3: {n1*n2*n3}')
