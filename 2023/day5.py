from pprint import pprint
# Solution assistance was from this repo:
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py
# video: https://youtu.be/iqTopXV13LE here.  Modified to use no class.

inp = []
with open("./input/day5.txt", "r") as f:
    inp = f.read()

seeds, *groups = inp.split("\n\n")
seeds = [int(x) for x in seeds.split(":")[1].split()]

sVals = seeds
for g in groups:
    lines = g.split("\n")[1:]
    group_mappings = [[int(x) for x in line.split()] for line in lines]
    updatedVals = []
    for s in sVals:
        for dest, src, sz in group_mappings:
            if src <= s < src + sz:
                updatedVals.append(s + dest - src)
                break
        else:
            updatedVals.append(s)

    sVals = updatedVals

print(min(sVals))

P2 = []
pairs = list(zip(seeds[::2], seeds[1::2]))
for st, sz in pairs:
    R = [(st, st + sz)]
    for g in groups:
        lines = g.split("\n")[1:]
        group_mappings = [[int(x) for x in line.split()] for line in lines]
        A = []
        # First time doing intervals, this breaks up a range and applies a mapping if there
        # is overlap
        for dest, src, sz in group_mappings:
            src_end = src + sz
            NR = []
            while R:
                st, ed = R.pop()
                before = st, min(ed, src)
                inter = max(st, src), min(src_end, ed)
                after = max(src_end, st), ed
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        R = R + A
    P2.append(min(R)[0])

print(min(P2))
