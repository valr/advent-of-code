#!/usr/bin/env python3

import queue

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

def run_boost(_input):
    que_in, que_out = queue.Queue(), queue.Queue()
    que_in.put(_input)

    cpu = Computer(que_in, que_out)
    cpu.load_file("./puzzle_9.input", 1024)
    cpu.run()

    return que_out.get()

print("BOOST keycode in test mode:", run_boost(1))
print("BOOST keycode in sensor boost mode:", run_boost(2))
