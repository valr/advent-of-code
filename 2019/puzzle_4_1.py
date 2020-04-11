#!/usr/bin/env python3

def check_password(p):
    adjacent = False

    i = 5
    while i:
        if p[i] < p[i-1]:
            return False
        if p[i] == p[i-1]:
            adjacent = True
        i -= 1

    if not adjacent:
        return False

    return True

#print(check_password(111111))
#print(check_password(223450))
#print(check_password(123789))

count = 0
for p in range(206938, 679129):
    if check_password(str(p)):
        count += 1

print("Passwords that meet the criteria:", count)
