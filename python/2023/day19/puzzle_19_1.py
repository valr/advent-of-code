#!/usr/bin/env python3


def process_workflow(workflow, parts):
    for rule in workflows[workflow]:
        if (
            not rule[0]
            or (rule[1] == ">" and parts[rule[0]] > rule[2])
            or (rule[1] == "<" and parts[rule[0]] < rule[2])
        ):
            return rule[3]

    raise Exception("no rule found")


with open("puzzle_19w.txt") as file:
    lines = file.read().splitlines()

workflows = {}
for line in lines:
    key, value = line.strip("}").split("{")
    value = [
        (
            rule[0] if ":" in rule else None,
            rule[1] if ":" in rule else None,
            int(rule[2:].split(":")[0]) if ":" in rule else None,
            rule[2:].split(":")[1] if ":" in rule else rule,
        )
        for rule in value.split(",")
    ]
    workflows[key] = value

with open("puzzle_19r.txt") as file:
    ratings = file.read().splitlines()

accepted_ratings = 0

for rating in ratings:
    parts = {
        r.split("=")[0]: int(r.split("=")[1]) for r in rating.strip("{}").split(",")
    }

    workflow = "in"
    while workflow != "A" and workflow != "R":
        workflow = process_workflow(workflow, parts)

    if workflow == "A":
        accepted_ratings += sum(parts.values())

print(f"accepted ratings: {accepted_ratings}")
