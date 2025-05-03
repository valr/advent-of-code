#!/usr/bin/env python3

def read_input(filename):
    with open(filename) as file:
        input = file.read().split('\n\n')

    return input


def get_result(input):
    return sum([len(set(s.replace('\n', ''))) for s in input])


if __name__ == '__main__':
    result = get_result(read_input('puzzle_6_1.txt'))
    print(f'sum of counts: {result}')
