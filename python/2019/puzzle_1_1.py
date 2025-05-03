#!/usr/bin/env python3

import fileinput

def compute_fuel(mass):
    return mass // 3 - 2

with fileinput.input() as file:
    total_fuel = sum(compute_fuel(int(line)) for line in file)

print(total_fuel)

#print(compute_fuel(12))
#print(compute_fuel(14))
#print(compute_fuel(1969))
#print(compute_fuel(100756))
