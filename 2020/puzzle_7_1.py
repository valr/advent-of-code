#!/usr/bin/env python3

with open('puzzle_7_1.txt') as file:
    lines = file.read().splitlines()

colors = set()


def count_bags(color):
    for line in lines:
        split = line.split(' bags contain ')
        if (color in split[1]):
            colors.add(split[0])
            count_bags(split[0])


if __name__ == '__main__':
    count_bags('shiny gold')
    print(f'bags containing shiny gold bag: {len(colors)}')
