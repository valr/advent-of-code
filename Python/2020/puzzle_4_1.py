#!/usr/bin/env python3

def read_passports(filename):
    with open(filename) as file:
        passports = file.read().split('\n\n')

    return passports


def validate_passports(passports):
    required_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    valid = 0
    for passport in passports:
        fields = dict(field.split(':', 1) for field in passport.split())
        if all(key in fields.keys() for key in required_keys):
            valid += 1

    return valid


if __name__ == '__main__':
    valid = validate_passports(read_passports('puzzle_4_1.txt'))
    print(f'number of valid passwords: {valid}')
