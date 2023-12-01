#!/usr/bin/env python3


def is_letter_digit(s):
    digits = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i in range(0, len(digits)):
        if s.startswith(digits[i]):
            return i + 1


with open("puzzle_1.txt") as file:
    lines = file.read().splitlines()

calibration_value = 0
for line in lines:
    first_digit, last_digit = None, None
    for i in range(0, len(line)):
        digit = int(line[i]) if line[i].isdigit() else is_letter_digit(line[i:])
        if digit:
            last_digit = digit
            if not first_digit:
                first_digit = digit
    calibration_value += first_digit * 10 + last_digit
print(calibration_value)
