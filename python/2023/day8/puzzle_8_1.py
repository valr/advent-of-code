#!/usr/bin/env python3

with open("puzzle_8.txt") as file:
    lines = (
        file.read()
        .replace("=", "")
        .replace("(", "")
        .replace(",", "")
        .replace(")", "")
        .splitlines()
    )

path = lines[0]
map = {node.split()[0]: [node.split()[1], node.split()[2]] for node in lines[2:]}

position = "AAA"
step_count = 0

while position != "ZZZ":
    for step in path:
        step_count += 1
        position = map[position][0 if step == "L" else 1]
        if position == "ZZZ":
            break

print(f"step count: {step_count}")
