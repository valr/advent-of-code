#!/usr/bin/env python3

from itertools import groupby

def check_password(p):

    i = 5
    while i:
        if p[i] < p[i-1]:
            return False
        i -= 1

    if 2 not in [len(''.join(c)) for _, c in groupby(p)]:
        return False

    return True

#print(check_password(112233))
#print(check_password(123444))
#print(check_password(111122))

count = 0
for p in range(206938, 679129):
    if check_password(str(p)):
        count += 1

print("Passwords that meet the criteria:", count)
