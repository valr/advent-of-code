#!/usr/bin/env python3

def add(p1, p2, p3):
    program[p3] = program[p1] + program[p2]
    return True

def mul(p1, p2, p3):
    program[p3] = program[p1] * program[p2]
    return True

def hlt(*none):
    return False

def instruction(ip):
    opcode = {1:add, 2:mul, 99:hlt}
    return opcode[program[ip]](*program[ip+1:ip+4])

def run():
    for ip in range(0, len(program), 4):
        if not instruction(ip):
            break
    return program[0]

program = [int(code) for code in open('puzzle_2_1.input').read().split(',')]
program[1:3] = [12, 2] # alarm 1202

print(run())
