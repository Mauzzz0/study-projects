mtrx = list()
for _ in range(int(input())):
    mtrx.append(input().split(","))
for _ in range(int(input())):
    g, g1 = input().split(',')
    g, g1 = int(g), int(g1)
    print(mtrx[g][g1])
