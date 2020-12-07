#!/usr/bin/env python3

with open('puzzle_7_2.txt') as file:
    rules = file.read().splitlines()


def count_bags(color):
    count = 0
    for rule in rules:
        rule = rule.replace(' bags', '').replace(' bag', '').replace('.', '')
        split = rule.split(' contain ')
        if color == split[0]:
            for contained_bag in split[1].split(', '):
                nb_bag, color_bag = contained_bag.split(' ', 1)
                if nb_bag != 'no':
                    count += int(nb_bag) + int(nb_bag) * count_bags(color_bag)
    return count


if __name__ == '__main__':
    count = count_bags('shiny gold')
    print(f'individual bags inside shiny gold bag: {count}')
