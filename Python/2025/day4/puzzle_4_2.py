#!/usr/bin/env python3

grid = []

with open("input.txt") as f:
    for line in f:
        grid.append("#" + line.strip() + "#")
    grid.insert(0, "#" * len(grid[0]))
    grid.append("#" * len(grid[0]))

old_count, count = -1, 0
while old_count != count:
    old_count, count = count, 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@" or grid[row][col] == "x":
                s = grid[row - 1][col - 1 : col + 2] + grid[row][col - 1 : col + 2] + grid[row + 1][col - 1 : col + 2]
                if s.count("@") <= 4:
                    count += 1
                    grid[row] = grid[row][:col] + "x" + grid[row][col + 1 :]

print(count)
