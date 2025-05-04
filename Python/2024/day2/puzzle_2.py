from operator import sub


def is_safe(diffs: list[int]) -> bool:
    return all(1 <= x <= 3 for x in diffs) or all(-3 <= x <= -1 for x in diffs)


with open("input.txt") as f:
    reports = list(list(map(int, line.split())) for line in f)

safe_reports, dampen_safe_reports = 0, 0

for r in reports:
    diffs = list(map(sub, r[:-1], r[1:]))
    if is_safe(diffs):
        safe_reports += 1
    else:
        for i in range(len(r)):
            dampen_r = r[:i] + r[i + 1 :]
            diffs = list(map(sub, dampen_r[:-1], dampen_r[1:]))
            if is_safe(diffs):
                dampen_safe_reports += 1
                break

print(f"safe reports: {safe_reports}")
print(f"safe reports with problem dampener: {safe_reports + dampen_safe_reports}")
