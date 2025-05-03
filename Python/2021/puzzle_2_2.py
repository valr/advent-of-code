#!/usr/bin/env python3

position, depth, aim = 0, 0, 0

with open("puzzle_2_2.txt") as file:
    for line in file:
        command, unit = line.split(" ")
        unit = int(unit)
        # quick and dirty, as usual for AoC
        if command == "forward":
            position += unit
            depth += aim * unit
        elif command == "down":
            aim += unit
        elif command == "up":
            aim -= unit

print(f"final horizontal position multiplied by final depth: {position * depth}")
