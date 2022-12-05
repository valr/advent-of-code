#!/usr/bin/env python3


def build_stacks(stacks, line):
    for i in range(1, len(line), 4):
        if line[i : i + 1].strip():
            stacks[i // 4].insert(0, line[i : i + 1])


def move_stacks1(stacks, crates, stack_from, stack_to):
    for i in range(1, crates + 1):
        stacks[stack_to - 1].append(stacks[stack_from - 1].pop())


def move_stacks2(stacks, crates, stack_from, stack_to):
    for crate in stacks[stack_from - 1][-crates:]:
        stacks[stack_to - 1].append(crate)
    stacks[stack_from - 1] = stacks[stack_from - 1][:-crates]


def print_stacks(stacks):
    print("".join([stack[-1:][0] for stack in stacks if stack[-1:]]))


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
        build_stacks(stacks, line)

print_stacks(stacks)
