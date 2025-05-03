#!/usr/bin/env python3

import queue
import threading

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

def run_hull_painting_robot(array, len_x, len_y, start):

    def pos(y, x):
        return (y * len_x) + x

    que_in, que_out = queue.Queue(), queue.Queue()

    cpu = Computer(que_in, que_out)
    cpu.load_file("./puzzle_11.input", 1024)

    thr = threading.Thread(target=cpu.run)
    thr.start()

    pos_x, pos_y = len_x // 2, len_y // 2
    step_x, step_y = 0, 1
    direction = 0

    array[pos(pos_y, pos_x)] = start

    while thr.is_alive():
        que_in.put(array[pos(pos_y, pos_x)] % 2)

        c = que_out.get()
        if c == 0:
            array[pos(pos_y, pos_x)] = 2
        if c == 1:
            array[pos(pos_y, pos_x)] = 1

        d = que_out.get()
        if d == 0:
            direction = (direction - 1 + 4) % 4
        if d == 1:
            direction = (direction + 1) % 4

        if direction == 0:
            step_x, step_y = 0, 1
        elif direction == 1:
            step_x, step_y = 1, 0
        elif direction == 2:
            step_x, step_y = 0, -1
        elif direction == 3:
            step_x, step_y = -1, 0

        pos_x += step_x
        pos_y += step_y

x, y = 80, 80

hull = [0] * x * y
run_hull_painting_robot(hull, x, y, 0)

print("Number of panels painted at least once:", (x * y) - hull.count(0))

hull = [0] * x * y
run_hull_painting_robot(hull, x, y, 1)

print("Registration identifier:")

for yy in range(45, 30, -1):
    for xx in range(x):
        print(str(hull[(yy * x) + xx]).replace('0', ' ').replace('2', ' ').replace('1', '#'), end = '')
    print()
