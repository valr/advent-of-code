#!/usr/bin/env python3

import fileinput

def compute_fuel(mass):
    while True:
        fuel = mass // 3 - 2
        if fuel > 0:
            yield fuel
            mass = fuel
        else:
            break

with fileinput.input() as file:
    total_fuel = sum(sum(compute_fuel(int(line))) for line in file)

print(total_fuel)

#print(sum(compute_fuel(14)))
#print(sum(compute_fuel(1969)))
#print(sum(compute_fuel(100756)))
