#!/usr/bin/env python3

import queue
import threading
import time

class Computer:
    def __init__(self, _input, output):
        self.instruction = { # opcode: method, instruction size
            1: (self.add, 4),
            2: (self.mul, 4),
            3: (self.inp, 2),
            4: (self.out, 2),
            5: (self.jmt, 3),
            6: (self.jmf, 3),
            7: (self.lss, 4),
            8: (self.equ, 4),
            9: (self.rbo, 2),
            99:(self.hlt, 1)}

        self.ip = 0
        self.rb = 0
        self.memory = []
        self.input = _input
        self.output = output

    def load_file(self, program, extra_memory=0):
        self.load_memory(
            [int(i) for i in open(program).read().split(',')], extra_memory)

    def load_memory(self, memory, extra_memory=0):
        self.memory = memory + ([0] * extra_memory)

    def run(self):
        while True:
            instru = "00000" + str(self.memory[self.ip])
            method, size = self.instruction[int(instru[-2:])]
            method(*self.memory[self.ip + 1:self.ip + size], # parameters
                   *instru[-5:-2][:-size:-1]) # modes

            if method == self.hlt:
                break

            self.ip += size

    # 0 = position mode
    # 1 = immediate mode (not for address)
    # 2 = relative mode

    def address(self, parameter, mode):
        if mode == '0':
            return parameter
        else:
            return parameter + self.rb

    def value(self, parameter, mode):
        if mode == '1':
            return parameter
        else:
            return self.memory[self.address(parameter, mode)]

    def add(self, p1, p2, p3, m1, m2, m3):
        self.memory[self.address(p3, m3)] = self.value(p1, m1) + self.value(p2, m2)

    def mul(self, p1, p2, p3, m1, m2, m3):
        self.memory[self.address(p3, m3)] = self.value(p1, m1) * self.value(p2, m2)

    def inp(self, p1, m1):
        self.memory[self.address(p1, m1)] = self.input.get()

    def out(self, p1, m1):
        self.output.put(self.value(p1, m1))

    def jmt(self, p1, p2, m1, m2):
        if self.value(p1, m1) != 0:
            self.ip = self.value(p2, m2) - self.instruction[5][1]

    def jmf(self, p1, p2, m1, m2):
        if self.value(p1, m1) == 0:
            self.ip = self.value(p2, m2) - self.instruction[6][1]

    def lss(self, p1, p2, p3, m1, m2, m3):
        if self.value(p1, m1) < self.value(p2, m2):
            self.memory[self.address(p3, m3)] = 1
        else:
            self.memory[self.address(p3, m3)] = 0

    def equ(self, p1, p2, p3, m1, m2, m3):
        if self.value(p1, m1) == self.value(p2, m2):
            self.memory[self.address(p3, m3)] = 1
        else:
            self.memory[self.address(p3, m3)] = 0

    def rbo(self, p1, m1):
        self.rb += self.value(p1, m1)

    def hlt(self):
        pass

def run_arcade_cabinet1(program):
    queue_in, queue_out = queue.Queue(), queue.Queue()

    cpu = Computer(queue_in, queue_out)
    cpu.load_file(program, 1024)
    cpu.run()

    block_count = 0
    while not queue_out.empty():
        x, y, value = queue_out.get(), queue_out.get(), queue_out.get()

        if value == 2:
            block_count += 1

    return block_count

def display_arcade_screen(screen):
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')

    for y in range(25):
        for x in range(80):
            value = screen[(y * 80) + x]

            if value == 1:
                print('#', end='')
            elif value == 2:
                print('¤', end='')
            elif value == 3:
                print('_', end='')
            elif value == 4:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def run_arcade_cabinet2(program, delay):
    queue_in, queue_out = queue.Queue(), queue.Queue()

    cpu = Computer(queue_in, queue_out)
    cpu.load_file(program, 1024)

    thread = threading.Thread(target=cpu.run)
    thread.start()

    screen = [0] * 80 * 25
    score, block, ball, paddle = 0, 0, 0, 0

    while True:
        time.sleep(delay)

        while not queue_out.empty():
            x, y, value = queue_out.get(), queue_out.get(), queue_out.get()

            if x == -1 and y == 0:
                score = value
            else:
                screen[(y * 80) + x] = value

            if value == 3:
                paddle = x
            elif value == 4:
                ball = x

        display_arcade_screen(screen)

        if screen.count(2) == 0:
            break

        if paddle < ball:
            queue_in.put(1)
        elif paddle > ball:
            queue_in.put(-1)
        else:
            queue_in.put(0)

    return score

print("Number of block tiles on the screen when the game exits:", run_arcade_cabinet1("./puzzle_13_1.input"))

# the input file for part 2 is the same as input file for part 1 with very first digit set to 2 (play for free)
print("Score after the last block is broken:", run_arcade_cabinet2("./puzzle_13_2.input", 0.1)) # delay set to 0.1, be patient (or reduce the delay)
