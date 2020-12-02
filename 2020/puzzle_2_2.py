#!/usr/bin/env python3

import re

valid = 0
with open('puzzle_2_2.txt') as file:
    for line in file:
        pos1, pos2, char, password, _ = re.split(r' |-|: |\n', line)
        pos1, pos2 = int(pos1)-1, int(pos2)-1

        if (password[pos1] == char or password[pos2] == char) and \
            password[pos1] != password[pos2]:
            valid = valid+1

print(f'count of valid passwords: {valid}')
