#!/usr/bin/env python3

from itertools import permutations
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
            99:(self.hlt, 1)}

        self.ip = 0
        self.memory = []
        self.input = _input
        self.output = output

    def load_file(self, program):
        self.memory = [int(i) for i in open(program).read().split(',')]

    def load_memory(self, memory):
        self.memory = memory

    def run(self):
        while True:
            instru = "00000" + str(self.memory[self.ip])
            method, size = self.instruction[int(instru[-2:])]
            method(*self.memory[self.ip + 1:self.ip + size], # parameters
                   *instru[-5:-2][:-size:-1]) # modes

            if method == self.hlt:
                break

            self.ip += size

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
        self.memory[p1] = self.input.get()

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

def run_amp(phase):
    count = len(phase)
    que, amp, thr = [], [], []

    for i in range(count):
        que.append(queue.Queue())
        que[i].put(phase[i])

    for i in range(count):
        amp.append(Computer(que[i], que[(i+1)%5]))
        amp[i].load_file("./puzzle_7.input")
        thr.append(threading.Thread(target=amp[i].run))

    que[0].put(0) # initial signal

    for i in range(5):
        thr[i].start()

    for i in range(5):
        thr[i].join()

    return que[0].get() # final signal

print("Highest signal for part 1:",
      max([run_amp(phase) for phase in permutations([0, 1, 2, 3, 4], 5)]))

print("Highest signal for part 2:",
      max([run_amp(phase) for phase in permutations([5, 6, 7, 8, 9], 5)]))
