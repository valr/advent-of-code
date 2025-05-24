import re

with open("input.txt") as file:
    line = file.read()
    size = len(line.split()[0])

regex = []
for i in [0, *range(size - 1, size + 2)]:
    regex.append(f"(?=(X{'.' * i}M{'.' * i}A{'.' * i}S))")
    regex.append(f"(?=(S{'.' * i}A{'.' * i}M{'.' * i}X))")

count1 = sum(map(lambda x: len(re.findall(x, line, re.DOTALL)), regex))
print(f"solution 1: {count1}")

dotline = "." * (size - 1)
regex = [
    f"(?=(M.S{dotline}A{dotline}M.S))",
    f"(?=(S.S{dotline}A{dotline}M.M))",
    f"(?=(M.M{dotline}A{dotline}S.S))",
    f"(?=(S.M{dotline}A{dotline}S.M))",
]

count2 = sum(map(lambda x: len(re.findall(x, line, re.DOTALL)), regex))
print(f"solution 2: {count2}")
