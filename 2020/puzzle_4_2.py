#!/usr/bin/env python3

import re


def read_passports(filename):
    with open(filename) as file:
        passports = file.read().replace('\n\n', '\t').replace('\n', ' ').split('\t')

    return passports


def validate_field(key, value):
    if key == 'byr':
        return value.isdigit() and (1920 <= int(value) <= 2002)
    if key == 'iyr':
        return value.isdigit() and (2010 <= int(value) <= 2020)
    if key == 'eyr':
        return value.isdigit() and (2020 <= int(value) <= 2030)
    if key == 'hgt':
        height, unit = value[:-2], value[-2:]
        if unit == 'cm' and height.isdigit() and (150 <= int(height) <= 193):
            return True
        elif unit == 'in' and height.isdigit() and (59 <= int(height) <= 76):
            return True
        else:
            return False
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
    passports = read_passports('puzzle_4_2.txt')
    valid = validate_passports(passports)

    print(f'number of valid passwords: {valid}')
