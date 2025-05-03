#!/usr/bin/env python3

image = open('puzzle_8.input').readline()

x, y = 25, 6
z = len(image) // x // y

def count(z, c):
    return len([i for i in image[x*y*z:x*y*(z+1)] if i == c])

i = [count(i, '0') for i in range(z)]
i = i.index(min(i))

print("Result for part 1:", count(i, '1') * count(i, '2'))
print("Result for part 2:")

for yy in range(y):
    for xx in range(x):
        l = [[i for i in image[(zz*y*x)+(yy*x)+xx:(zz*y*x)+(yy*x)+xx+1] if i != '2'] for zz in range(z)]
        print([i for i in l if i][0][0].replace('0',' ').replace('1','#'), end='')
    print()
