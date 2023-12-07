inp = []
with open("./input/day6.txt", "r") as f:
    T = f.readline().split(":")[1].split()
    D = f.readline().split(":")[1].split()

p1 = zip(
    [int(x) for x in T],
    [int(x) for x in D]
)
p2 = (
    int("".join(T)),
    int("".join(D)),
)
print(p2)

options = []
for (t, dist) in p1:
    count = 0
    for et in range(1, t+1):
        if (t - et) * et >= dist:
            count += 1

    options.append(count)

total = 1
for n in options:
    total *= n

options = []
(t, dist)= p2
count = 0
for et in range(1, t+1):
    if (t - et) * et >= dist:
        count += 1

options.append(count)

total = 1
for n in options:
    total *= n

print(total)