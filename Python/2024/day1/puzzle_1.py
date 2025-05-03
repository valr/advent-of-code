from operator import mul

with open("input.txt") as f:
    l1, l2 = zip(*(map(int, line.split()) for line in f))

total_distance = sum(map(lambda x, y: abs(x - y), sorted(l1), sorted(l2)))
print(f"total distance: {total_distance}")

total_similarity_score = sum(map(mul, l1, map(l2.count, l1)))
print(f"total similarity score: {total_similarity_score}")
