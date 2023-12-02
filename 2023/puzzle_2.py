#!/usr/bin/env python3

import math
import re

with open("puzzle_2.txt") as file:
    lines = file.read().splitlines()

sum_game_id, sum_power_sets = 0, 0
for line in lines:
    game = re.split(":|;", line)
    game_id = int(game[0].split()[-1])
    power_sets = {}
    for sets in game[1:]:
        colors = {
            key: int(value)
            for value, key in (pair.split() for pair in sets.strip().split(", "))
        }

        # game not possible if the bag contained
        # only 12 red cubes, 13 green cubes, and 14 blue cubes
        if not (
            colors.get("red", 0) <= 12
            and colors.get("green", 0) <= 13
            and colors.get("blue", 0) <= 14
        ):
            game_id = 0

        # fewest number of cubes of each color that could have been in the bag
        # to make the game possible
        for color in ["red", "green", "blue"]:
            power_sets[color] = max(power_sets.get(color, 0), colors.get(color, 0))

    sum_game_id += game_id
    sum_power_sets += math.prod(power_sets.values())
print(f"sum_game_id: {sum_game_id}")
print(f"sum_power_sets: {sum_power_sets}")
