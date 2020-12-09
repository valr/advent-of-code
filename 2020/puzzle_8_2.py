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
            return False, accumulator

        if op == 'acc':
            accumulator += arg
            ip += 1
        elif op == 'jmp':
            ip += arg
        else:
            ip += 1

    return True, accumulator


if __name__ == '__main__':
    instructions = read_instructions('puzzle_8_2.txt')

    for ip in range(len(instructions)):
        instructions_copy = instructions[:]

        if instructions_copy[ip][:3] == 'jmp':
            instructions_copy[ip] = 'nop' + instructions_copy[ip][3:]
        elif instructions_copy[ip][:3] == 'nop':
            instructions_copy[ip] = 'jmp' + instructions_copy[ip][3:]
        else:
            continue

        status, accumulator = run_instructions(instructions_copy)
        if status:
            break

    print(f'accumulator: {accumulator}')
