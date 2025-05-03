#!/usr/bin/env python3

import re

valid = 0
with open('puzzle_2_1.txt') as file:
    for line in file:
        min_, max_, char, password, _ = re.split(r' |-|: |\n', line)
        count = password.count(char)
        if count >= int(min_) and count <= int(max_):
            valid += 1

print(f'count of valid passwords: {valid}')
