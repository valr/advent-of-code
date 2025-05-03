#!/usr/bin/env python3

import re


def read_passports(filename):
    with open(filename) as file:
        passports = file.read().split('\n\n')

    return passports


def validate_field(key, value):
    if key == 'byr':
        return 1920 <= int(value) <= 2002
    if key == 'iyr':
        return 2010 <= int(value) <= 2020
    if key == 'eyr':
        return 2020 <= int(value) <= 2030
    if key == 'hgt':
        height, unit = value[:-2], value[-2:]
        return (unit == 'cm' and 150 <= int(height) <= 193) or \
            (unit == 'in' and 59 <= int(height) <= 76)
    if key == 'hcl':
        return re.match(r'^#[0-9a-f]{6}$', value)
    if key == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if key == 'pid':
        return re.match(r'^[0-9]{9}$', value)


def validate_passports(passports):
    required_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    valid = 0
    for passport in passports:
        fields = dict(field.split(':', 1) for field in passport.split())
        if all(validate_field(key, fields[key]) if key in fields.keys() else False for key in required_keys):
            valid += 1

    return valid


if __name__ == '__main__':
    valid = validate_passports(read_passports('puzzle_4_2.txt'))
    print(f'number of valid passwords: {valid}')
