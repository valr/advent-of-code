#!/usr/bin/env python3

def read_instructions(filename):
    with open(filename) as file:
        instructions = file.read().splitlines()

    return instructions


def run_instructions(instructions):
    ip, accumulator = 0, 0
    instruction_set = set()

    while(ip < len(instructions)):
        op, arg = instructions[ip].split()
        arg = int(arg)

        if ip not in instruction_set:
            instruction_set.add(ip)
        else:
            return accumulator

        if op == 'acc':
            accumulator += arg
            ip += 1
        elif op == 'jmp':
            ip += arg
        else:
            ip += 1


if __name__ == '__main__':
    accumulator = run_instructions(read_instructions('puzzle_8_1.txt'))
    print(f'accumulator: {accumulator}')
