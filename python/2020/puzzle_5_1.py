#!/usr/bin/env python3

def read_input(filename):
    with open(filename) as file:
        input = file.read().splitlines()

    return input


def binary_partitioning(s, lo, hi):
    half = (hi - lo + 1) // 2
    for c in s:
        if c in ('F', 'L'):
            hi -= half
        else:
            lo += half
        half //= 2

    return lo


def highest_seat_id(input):
    return max([binary_partitioning(boarding_pass[:7], 0, 127) * 8 +
                binary_partitioning(boarding_pass[7:], 0, 7)
                for boarding_pass in input])


if __name__ == '__main__':
    seat_id = highest_seat_id(read_input('puzzle_5_1.txt'))
    print(f'highest seat id on a boarding pass: {seat_id}')
