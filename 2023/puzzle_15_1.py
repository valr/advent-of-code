#!/usr/bin/env python3


def hash(str):
    h = 0
    for c in str:
        h = (h + ord(c)) * 17 % 256
    return h


with open("puzzle_15.txt") as file:
    sequence = file.read()

print("sum of hash:", sum([hash(step) for step in sequence.split(",")]))
