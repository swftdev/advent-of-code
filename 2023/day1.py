import functools as ft
import math as m

input = ""

with open("./input/day1.txt", "r") as f:
    input = f.readlines()

wordObj = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

foundPairs = []

for r in input:
    fna = None
    lnt = None
    fnwt = (m.inf, "")
    lnwt = (-m.inf, "")

    for i, l in enumerate(r):
        if l.isnumeric():
            if not fna:
                fna = (i, l)
            lnt = (i, l)

    for k, v in wordObj.items():
        fi = r.find(k)
        mri = r[::-1].find(k[::-1])
        li = (len(r) - mri) - 1

        if fi != -1 and fi < fnwt[0]: fnwt = (fi, k)
        if mri != -1 and li > lnwt[0]: lnwt = (li, k)

    firstValue = None
    lastValue = None

    if (fna[0] < fnwt[0]): firstValue = fna[1]
    else: firstValue = wordObj[fnwt[1]]

    if (lnt[0] > lnwt[0]): lastValue = lnt[1]
    else: lastValue = wordObj[lnwt[1]]

    foundPairs.append(int(firstValue + lastValue))
    
print(ft.reduce(lambda a, b: a + b ,foundPairs))
