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


def get_seat_id(input):
    seats = [binary_partitioning(boarding_pass[:7], 0, 127) * 8 +
             binary_partitioning(boarding_pass[7:], 0, 7)
             for boarding_pass in input]
    seats.sort()

    return [j-1 for i, j in zip(seats, seats[1:]) if j-i > 1][0]


if __name__ == '__main__':
    seat_id = get_seat_id(read_input('puzzle_5_1.txt'))
    print(f'the seat id: {seat_id}')
