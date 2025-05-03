#!/usr/bin/env python3

class Computer:
    def __init__(self, program = ""):
        self.instruction = { # opcode: method, instruction size
            1: (self.add, 4),
            2: (self.mul, 4),
            3: (self.inp, 2),
            4: (self.out, 2),
            5: (self.jmt, 3),
            6: (self.jmf, 3),
            7: (self.lss, 4),
            8: (self.equ, 4),
            99:(self.hlt, 1)}

        self.ip = 0
        self.memory = []
        self.input = 0
        self.output = 0

        if program:
            self.load_file(program)

    def load_file(self, program):
        self.memory = [int(i) for i in open(program).read().split(',')]

    def load_memory(self, memory):
        self.memory = memory

    def set_input(self, _input):
        self.input = int(_input)

    def get_output(self):
        return self.output

    def run(self):
        while True:
            instru = "00000" + str(self.memory[self.ip])
            method, size = self.instruction[int(instru[-2:])]
            method(*self.memory[self.ip + 1:self.ip + size], # parameters
                   *instru[-5:-2][:-size:-1]) # modes

            self.ip += size

            if method == self.hlt:
                break

    def value(self, parameter, mode):
        if mode == '0':
            return self.memory[parameter]
        else:
            return parameter

    def add(self, p1, p2, p3, m1, m2, m3):
        self.memory[p3] = self.value(p1, m1) + self.value(p2, m2)

    def mul(self, p1, p2, p3, m1, m2, m3):
        self.memory[p3] = self.value(p1, m1) * self.value(p2, m2)

    def inp(self, p1, m1):
        self.memory[p1] = self.input

    def out(self, p1, m1):
        self.output = self.value(p1, m1)

    def jmt(self, p1, p2, m1, m2):
        if self.value(p1, m1) != 0:
            self.ip = self.value(p2, m2) - self.instruction[5][1]

    def jmf(self, p1, p2, m1, m2):
        if self.value(p1, m1) == 0:
            self.ip = self.value(p2, m2) - self.instruction[6][1]

    def lss(self, p1, p2, p3, m1, m2, m3):
        if self.value(p1, m1) < self.value(p2, m2):
            self.memory[p3] = 1
        else:
            self.memory[p3] = 0

    def equ(self, p1, p2, p3, m1, m2, m3):
        if self.value(p1, m1) == self.value(p2, m2):
            self.memory[p3] = 1
        else:
            self.memory[p3] = 0

    def hlt(self):
        pass

computer1 = Computer('puzzle_5.input')
computer1.set_input(1)
computer1.run()
print("Part 1:", computer1.get_output())

computer2 = Computer('puzzle_5.input')
computer2.set_input(5)
computer2.run()
print("Part 2:", computer2.get_output())
