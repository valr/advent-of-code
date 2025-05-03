#!/usr/bin/env python3

with open("puzzle_3_1.txt") as file:
    bits = file.read().splitlines()

rotated_bits = list(zip(*bits[::-1]))

gamma = int("".join([max(b, key=b.count) for b in rotated_bits]), 2)
epsilon = int("".join([min(b, key=b.count) for b in rotated_bits]), 2)

print(f"Power consumption of the submarine: {gamma * epsilon}")
