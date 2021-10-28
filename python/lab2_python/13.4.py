stats = list()
tmp = list()
for _ in range(int(input())):
    tmp.append(int(input()))
stats.append([x for x in tmp])
stats.append([x for x in tmp])
for _ in range(int(input())):
    brat = int(input())
    stat = int(input())
    plus = int(input())
    stats[brat-1][stat] += plus
print(*stats[0], sep=" ")
print(*stats[1], sep=" ")
c = 0
for i in range(len(stats[0])):
    if stats[0][i] == stats[1][i]:
        c += 1
print(c)
