#!/usr/bin/env python3


def move_stacks1(stacks, crate, fr, to):
    for i in range(1, crate + 1):
        stacks[to - 1].append(stacks[fr - 1].pop())


def move_stacks2(stacks, crates, fr, to):
    stacks[to - 1] += stacks[fr - 1][-crates:]
    stacks[fr - 1] = stacks[fr - 1][:-crates]


with open("puzzle_5.txt") as file:
    lines = file.read().splitlines()

stacks = [[] for _ in range(9)]

for line in lines:
    if line.startswith("move"):
        # move_stacks1
        move_stacks2(
            stacks,
            *map(
                int,
                line.replace("move", "").replace("from", "").replace("to", "").split(),
            ),
        )
    elif line and not line.startswith(" 1 "):
        for i in range(1, len(line), 4):
            if line[i : i + 1].strip():
                stacks[i // 4].insert(0, line[i : i + 1])

print("".join([stack[-1:][0] for stack in stacks if stack[-1:]]))
