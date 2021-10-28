mtrx = list()
g = int(input())
[mtrx.append([0 for _ in range(g)]) for _ in range(g)]
for i in range(1, g):
    mtrx[i] = [int(x) for x in input().split(' ')]
_from, _to = [int(x) for x in input().split(' ')]
minim = mtrx[_to][_from]
peres = None
for i in range(g):
    per_cost = mtrx[i][_from]
    if per_cost != minim and per_cost != 0:
        # i = 2
        # from = 0
        # to = 1
        try:
            g = mtrx[i][_to]
            if g != 0:
                per_cost += g
                if per_cost < minim:
                    minim = per_cost
                    peres = i
        except: pass
print(peres)