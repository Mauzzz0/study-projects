mtrx = list()
medians = list()
mods = list()
for _ in range(int(input())):
    mtrx.append(sorted([int(x) for x in input().split(' ')]))
for i in range(len(mtrx)):
    print(mtrx[i][len(mtrx[i]) // 2], end=" ")
    medians.append(mtrx[i][len(mtrx[i]) // 2])
print()
for i in range(len(mtrx)):
    mx = max([mtrx[i].count(x) for x in mtrx[i]])
    for j in mtrx[i]:
        if mtrx[i].count(j) == mx:
            print(j, end=" ")
            mods.append(j)
            break
print()
print(medians[len(medians) // 2])
for i in range(len(mods)):
    mx = max([mods.count(x) for x in mods])
    if mods.count(mods[i]) == mx:
        print(mods[i])
        break
alls = list()
for j in mtrx:
    alls.extend(j)
alls = list(sorted(alls))
print(alls[len(alls)//2 +1])
for i in range(len(alls)):
    mx = max([alls.count(x) for x in alls])
    if alls.count(alls[i]) == mx:
        print(alls[i])
        break