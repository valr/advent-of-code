#!/usr/bin/env python3


def hash(str):
    h = 0
    for c in str:
        h = (h + ord(c)) * 17 % 256
    return h


with open("puzzle_15.txt") as file:
    sequence = file.read()

boxes = [[] for i in range(256)]

for step in sequence.split(","):
    if "-" in step:
        label = step.strip("-")
        box_id = hash(label)

        for lens_id, lens in enumerate(boxes[box_id]):
            if lens[0] == label:
                boxes[box_id].pop(lens_id)
    else:
        label, focal = [int(i) if i.isnumeric() else i for i in step.split("=")]
        box_id = hash(label)

        replaced = False
        for lens_id, lens in enumerate(boxes[box_id]):
            if lens[0] == label:
                boxes[box_id][lens_id] = (label, focal)
                replaced = True

        if not replaced:
            boxes[box_id].append((label, focal))

focusing_power = 0

for box_id, box in enumerate(boxes):
    for lens_id, lens in enumerate(boxes[box_id]):
        focusing_power += (box_id + 1) * (lens_id + 1) * lens[1]

print(f"focusing power: {focusing_power}")
