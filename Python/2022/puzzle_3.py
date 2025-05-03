#!/usr/bin/env python3

with open("puzzle_3.txt") as file:
    lines = file.read().splitlines()

priority = 0
for line in lines:
    mid = len(line) // 2
    type = (set(line[:mid]) & set(line[mid:])).pop()
    priority += ord(type) - 96 if type.islower() else ord(type) - 38
print(priority)

priority = 0
for i in range(0, len(lines), 3):
    type = (set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])).pop()
    priority += ord(type) - 96 if type.islower() else ord(type) - 38
print(priority)
