m = 4
n = 4

men = [0] * (m + 1)
friends = {}
friends[1] = [2]
friends[2] = [1, 3, 4]
friends[3] = [2, 4]
friends[4] = [2, 3]

men[1] = 1
day = 1

while True:
    sick = []
    sset = set()
    for i, m in enumerate(men):
        if m == 1:
            men[i] = 2
            sick.append(i)
        elif m == 2:
            men[i] = 0
    for s in sick:
        for f in friends[s]:
            sset.add(f)

    for t in sset:
        if men[i] == 0:
            men[i] = 1

    print(day, men, sick, sset)

    if all(x == 0 for x in men):
        break
    else:
        day = day + 1
