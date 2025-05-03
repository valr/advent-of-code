#!/usr/bin/env python3


def play_rps1(p1, p2):
    outcome = 0
    if (
        (p1 == "A" and p2 == "Z")
        or (p1 == "C" and p2 == "Y")
        or (p1 == "B" and p2 == "X")
    ):
        outcome = 0
    elif (
        (p1 == "A" and p2 == "X")
        or (p1 == "B" and p2 == "Y")
        or (p1 == "C" and p2 == "Z")
    ):
        outcome = 3
    else:
        outcome = 6
    return outcome, ord(p2) - 87


def play_rps2(p1, p2):
    lose = {"A": 3, "B": 1, "C": 2}
    draw = {"A": 1, "B": 2, "C": 3}
    win = {"A": 2, "B": 3, "C": 1}

    outcome, shape = 0, 0
    if p2 == "X":
        outcome = 0
        shape = lose[p1]
    elif p2 == "Y":
        outcome = 3
        shape = draw[p1]
    else:
        outcome = 6
        shape = win[p1]

    return outcome, shape


with open("puzzle_2.txt") as file:
    lines = file.read().splitlines()

score1, score2 = 0, 0
for line in lines:
    player1, player2 = line.split()
    score1 += sum(play_rps1(player1, player2))
    score2 += sum(play_rps2(player1, player2))

print(score1, score2)
