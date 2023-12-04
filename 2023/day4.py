from pprint import pprint 
inp = []
with open("./input/day4.txt", "r") as f:
    inp = [x.rstrip() for x in f.readlines()]

total = 0
cardWinCount = {}
cardTotals = { i + 1: 1 for i, _ in enumerate(inp)}
for i, r in enumerate(inp):
    f, s = r.split("|")
    f = [int(x) for x in f.split(":")[1].split(" ") if x]
    s = [int(x) for x in s.split(" ") if x]

    matches = len(set(f) & set(s))
    cardWinCount[i + 1] = matches
    if not matches: continue
    total += 2 ** (matches - 1)

for k, v in cardTotals.items():
    dist = cardWinCount[k]
    for j in range(v):
        for i in range(1, dist + 1):
            cardTotals[k + i] += 1

print("Part1:", total)
print("Part2:", sum(cardTotals.values()))