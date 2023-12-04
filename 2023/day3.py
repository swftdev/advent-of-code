from pprint import pprint

inp = []
with open("./input/day3.txt", "r") as f:
    inp = [x.strip() for x in f.readlines()]

rowCount = len(inp)
rowLen = len(inp[0])  # get max row len
symbols = "!\"#$%&'()*+,-/:;<=>?@[\\]^_`{|}~\n"
numbers = "1234567890"


def find_diag_matches(gp, row):
    coll = []
    if gp > 0:
        le = gp - 1
        ld = row[le] in numbers
        if ld:
            res = []
            for l in row[le::-1]:
                if not (l in numbers):
                    break
                res.append(l)
            res.reverse()
            coll.append("".join(res))

    if gp < rowLen - 1:
        rs = gp + 1
        rd = row[gp + 1] in numbers
        if rd:
            res = []
            for l in row[rs:]:
                if not (l in numbers):
                    break
                res.append(l)
            coll.append("".join(res))

    return [int(f) for f in coll]


if __name__ == "__main__":
    placeholder = "." * (rowLen)
    numbersToSum = []
    longestNum = 0
    for i, r in enumerate(inp):
        allNumbersToCheck = []
        start = -1
        end = -1
        for j, l in enumerate(r):
            if l in numbers:
                if start == -1:
                    start = j
                end = j
            else:
                if start != -1:
                    allNumbersToCheck.append((r[start : end + 1], start, end))
                    start = -1
                    end = -1

        if start != -1:
            allNumbersToCheck.append((r[start : end + 1], start, end))
        p = inp[i - 1] if i > 0 else placeholder
        n = inp[i + 1] if i + 1 < rowCount else placeholder

        for num, start, end in allNumbersToCheck:
            numLen = end - start + 1
            if numLen > longestNum:
                longestNum = numLen
            rs = start - 1 if start > 0 else 0
            re = end + 1 if start < rowLen else end
            scanRow = p[rs : re + 1] + r[rs : re + 1] + n[rs : re + 1]
            for c in scanRow:
                if c in symbols:
                    numbersToSum.append(int(num))
                    break

    print("Part 1:", sum(numbersToSum))

    gearRatioPairs = []
    for i, r in enumerate(inp):
        gearPosLocations = []
        for j, l in enumerate(r):
            if l == "*":
                gearPosLocations.append(j)

        p = inp[i - 1] if i > 0 else placeholder
        n = inp[i + 1] if i + 1 < rowCount else placeholder

        for gp in gearPosLocations:
            tmc = p[gp] in numbers
            bmc = n[gp] in numbers
            coll = []
            # handle top
            if tmc:
                tRegion = list(p[gp - numLen : gp + numLen])
                for k, c in enumerate(tRegion):
                    if c in symbols:
                        tRegion[k] = "."
                rowOps = "".join(tRegion).split(".")
                vals = []
                for op in rowOps:
                    if op:
                        vals.append(int(op))

                coll.append(max(vals))
            else:
                res = find_diag_matches(gp, p)
                coll = coll + res

            # handle mid
            res = find_diag_matches(gp, r)
            coll = coll + res

            # handle bot
            if bmc:
                bRegion = list(n[gp - numLen : gp + numLen])
                for k, c in enumerate(bRegion):
                    if c in symbols:
                        bRegion[k] = "."
                rowOps = "".join(bRegion).split(".")
                vals = []
                for op in rowOps:
                    if op:
                        vals.append(int(op))
                coll.append(max(vals))

            else:
                res = find_diag_matches(gp, n)
                coll = coll + res

            if len(coll) == 2:
                gearRatioPairs.append((int(coll[0]), int(coll[1])))

    print("Part 2:", sum([x * y for x, y in gearRatioPairs]))
