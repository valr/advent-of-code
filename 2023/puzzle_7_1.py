#!/usr/bin/env python3

from functools import cmp_to_key


def is_card_higher(card1, card2):
    strength = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    return strength.index(card1) - strength.index(card2)


def is_hand_higher(hand1, hand2):
    type1, type2 = get_type(hand1), get_type(hand2)
    if type1 == type2:
        for i in range(5):
            if hand1[i] != hand2[i]:
                return is_card_higher(hand1[i], hand2[i])
        return 0
    else:
        return type1 - type2


def get_type(hand):
    count = {card: hand.count(card) for card in hand}
    count = dict(sorted(count.items(), key=lambda c: c[1], reverse=True))

    for c in count:
        if count[c] == 5:
            return 6
        elif count[c] == 4:
            return 5
        elif count[c] == 3 and len(count) == 2:
            return 4
        elif count[c] == 3:
            return 3
        elif count[c] == 2 and len(count) == 3:
            return 2
        elif count[c] == 2:
            return 1
        else:
            return 0


with open("puzzle_7.txt") as file:
    lines = file.read().splitlines()

hands = [[i.split()[0], int(i.split()[1])] for i in lines]
sorted_hands = sorted(
    hands,
    key=cmp_to_key(lambda x, y: is_hand_higher(x[0], y[0])),
)

total_winnings = 0
for hand_ix, hand in enumerate(sorted_hands):
    total_winnings += hand[1] * (hand_ix + 1)
print(f"total winnings: {total_winnings}")
