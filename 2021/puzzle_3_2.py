#!/usr/bin/env python3


def get_rating(bits, most_common=True, prefix=""):
    rotated_bits = list(zip(*bits[::-1]))
    position = len(prefix)

    count_one = rotated_bits[position].count("1")
    count_zero = rotated_bits[position].count("0")

    prefix = prefix + (
        ("1" if count_one >= count_zero else "0")
        if most_common
        else ("0" if count_one >= count_zero else "1")
    )

    bits = [num for num in bits if num.startswith(prefix)]

    if len(bits) == 1:
        return int(bits[0], 2)
    else:
        return get_rating(bits, most_common, prefix)


with open("puzzle_3_2.txt") as file:
    bits = file.read().splitlines()

print(
    "Life support rating of the submarine:",
    get_rating(bits) * get_rating(bits, most_common=False),
)
