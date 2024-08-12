#!/usr/bin/env python3

from math import lcm

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
nodes = {node.split()[0]: [node.split()[1], node.split()[2]] for node in lines[2:]}

step_counts = []

for node in nodes:
    if node[2] == "A":
        position = node
        step_count = 0

        while position[2] != "Z":
            for step in path:
                step_count += 1
                position = nodes[position][0 if step == "L" else 1]
                if position[2] == "Z":
                    break

        step_counts.append(step_count)

print(f"step counts: {lcm(*step_counts)}")
