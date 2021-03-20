dic = dict()
for _ in range(int(input())):
    g1, g2 = input().split(' ')
    ar = dic.get(g2, [])
    ar.append(g1)
    dic[g2] = ar
for _ in range(int(input())):
    res = dic.get(input(), "error")
    print(*res, sep=" ")
