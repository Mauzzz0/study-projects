mtrx = list()
g = int(input())
[mtrx.append([0 for j in range(g)]) for x in range(g)]
for i in range(g):
    for j in range(g):
        mtrx[i][j] = int(input())

for _ in range(int(input())):
    x, y = int(input()), int(input())
    mtrx[x][y] -= 8
    if y !=0:
        mtrx[x][y-1] -= 4
    mtrx[x][y+1] -= 4
    if x!=0:
        mtrx[x-1][y] -= 4
    mtrx[x+1][y] -= 4
    if x!=0 and y !=0:
        mtrx[x-1][y-1] -= 4
    mtrx[x+1][y+1] -= 4
    if y !=0:
        mtrx[x+1][y-1] -= 4
    if x!=0:
        mtrx[x-1][y+1] -= 4
for i in range(g):
    for j in range(g):
        if mtrx[i][j] < 0:
            mtrx[i][j] = 0
for el in mtrx:
    print(*el, sep=" ")

