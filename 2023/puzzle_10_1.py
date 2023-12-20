#!/usr/bin/env python3

with open("puzzle_10.txt") as file:
    lines = file.read().splitlines()

for line_ix, line in enumerate(lines):
    if "S" in line:
        posy = line_ix
        posx = line.index("S")

movy, movx = 0, 1  # first move to the right
posy += movy
posx += movx
steps = 1

while lines[posy][posx] != "S":
    curr = lines[posy][posx]
    if curr == "L":
        if movx != 0:
            movy, movx = -1, 0
        else:
            movy, movx = 0, 1
    elif curr == "J":
        if movx != 0:
            movy, movx = -1, 0
        else:
            movy, movx = 0, -1
    elif curr == "7":
        if movx != 0:
            movy, movx = 1, 0
        else:
            movy, movx = 0, -1
    elif curr == "F":
        if movx != 0:
            movy, movx = 1, 0
        else:
            movy, movx = 0, 1

    posy += movy
    posx += movx
    steps += 1

print(f"steps to the point farthest from the starting position: {int(steps / 2)}")
