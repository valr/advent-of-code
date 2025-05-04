from re import findall

with open("input.txt") as f:
    memory = f.read()

sum_of_multiplications = sum(int(x) * int(y) for x, y in findall(r"mul\((\d+),(\d+)\)", memory))
print(f"sum of the results of the multiplications: {sum_of_multiplications}")

sum_of_enabled_multiplications = 0
enabled_multiplications = True

for x, y, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", memory):
    if do:
        enabled_multiplications = True
    elif dont:
        enabled_multiplications = False
    elif enabled_multiplications:
        sum_of_enabled_multiplications += int(x) * int(y)

print(f"sum of the results of the enabled multiplications: {sum_of_enabled_multiplications}")
