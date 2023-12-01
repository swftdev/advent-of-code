import functools as ft
import math as m

input = []
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

numbers = []

for r in input:
    # Will be tuples holding found (index, value)
    fnt = None
    lnt = None

    for i, l in enumerate(r):
        if l.isnumeric():
            # First instance of number
            if not fnt:
                fnt = i, l
            lnt = i, l

    fwt = m.inf, ""
    lwt = -m.inf, ""

    for k, v in wordObj.items():
        fi = r.find(k) # First Index
        mri = r[::-1].find(k[::-1]) # Reversed last index
        li = (len(r) - mri) - 1 # Last Index

        # Found match and is closer to beginning
        if fi != -1 and fi < fwt[0]: fwt = fi, k

        # Found match and is closer to end
        if mri != -1 and li > lwt[0]: lwt = li, k

    # First occurrence of number or number word (based on index)
    fv = fnt[1] if (fnt[0] < fwt[0]) else wordObj[fwt[1]]
    # Last occurrence of number or number word (based on index)
    lv = lnt[1] if (lnt[0] > lwt[0]) else wordObj[lwt[1]]

    numbers.append(int(fv + lv))
    
print(ft.reduce(lambda a, b: a + b, numbers))