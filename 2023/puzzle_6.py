#!/usr/bin/env python3

with open("puzzle_6.txt") as file:
    lines = file.read().splitlines()

# part 1
time = [int(i) for i in lines[0].split()[1:]]
distance = [int(i) for i in lines[1].split()[1:]]

# part 2
# time = [int("".join(lines[0].split()[1:]))]
# distance = [int("".join(lines[1].split()[1:]))]

num_record = 1
for race_ix in range(len(time)):
    record = 0
    for time_ix in range(time[race_ix] + 1):
        travel = time_ix * (time[race_ix] - time_ix)
        if travel > distance[race_ix]:
            record += 1
    num_record *= record
print(f"number of ways you can beat the record: {num_record}")
