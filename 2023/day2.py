import functools as ft
def cleanRow(r):
    (f, s) = r.split(":")
    _, gameNumber = f.split()

    turnsStr = s.split(";")
    turns = []
    for t in turnsStr:
        turn = []
        for rev in t.split(","):
            rev = rev.strip()
            turn.append(rev)
        turns.append(turn)
    
    return gameNumber, turns

if __name__ == "__main__":
    input = []
    with open("./input/day2.txt", "r") as f:
        input = f.readlines()

    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    validScore = 0
    rowMaxProductSum = 0
    for r in input:
        gameNumber, turns = cleanRow(r)
        rowMax = { "green": 0, "blue": 0, "red": 0 }

        validGame = True
        for turn in turns:
            for dType in turn:
                count, color = dType.split(" ")
                count = int(count)
                if count > rowMax[color]: rowMax[color] = count
                if count > max_cubes[color]: validGame = False

        rowMaxProductSum += ft.reduce(lambda a, b: a * b, rowMax.values())
        if validGame: validScore += int(gameNumber)

    print(validScore)
    print(rowMaxProductSum)
