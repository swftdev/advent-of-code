from pprint import pprint 
from functools import cmp_to_key

with open("./input/day7.txt", "r") as f:
    inp = [x.rstrip().split() for x in f.readlines()]
    inp = [(h, int(v)) for (h, v) in inp]

letterValues = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

def orderHands(a, b):
    for i in range(5):
        al = letterValues[a[0][i]] 
        bl = letterValues[b[0][i]]
        if al > bl: return 1
        if bl > al: return -1

def getScore(cardCounts):
    cardCountLen = len(cardCounts)
    if cardCountLen == 1:
        return "Five of a kind"
    if cardCountLen == 2:
        if 4 in cardCounts:
            return "Four of a kind"
        return "Full House"
    elif cardCountLen == 3:
        if 3 in cardCounts:
            return "Three of a kind"
        return "Two Pair"
    elif cardCountLen == 4:
        return "One Pair"
    return "High Card"


groupedHands = { }
for handTup in inp:
    hand, val = handTup 
    cards = { }
    for i in hand:
        if cards.get(i):
            cards[i] += 1
        else:
            cards[i] = 1

    cardCounts = sorted(cards.values(), reverse=True)
    handOutcome = getScore(cardCounts)

    if grouping := groupedHands.get(handOutcome):
        grouping.append(handTup)
    else:
        groupedHands[handOutcome] = [handTup]

for k, g in groupedHands.items():
    g.sort(key=cmp_to_key(orderHands))


fullyOrderedArr = []
for h in handOrder:
    fullyOrderedArr += groupedHands[h]

total = 0
for i, h in enumerate(fullyOrderedArr):
    total += h[1] * (i + 1)

print(total)