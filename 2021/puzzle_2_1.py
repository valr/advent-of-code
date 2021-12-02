#!/usr/bin/env python3

position, depth = 0, 0

with open("puzzle_2_1.txt") as file:
    for line in file:
        command, unit = line.split(" ")
        unit = int(unit)
        # quick and dirty, as usual for AoC
        if command == "forward":
            position += unit
        elif command == "down":
            depth += unit
        elif command == "up":
            depth -= unit

print(f"final horizontal position multiplied by final depth: {position * depth}")
