prods = [input() for _ in range(int(input()))]
n = int(input())
for _ in range(n):
    title = input()
    ings = list()
    for __ in range(int(input())):
        ings.append(input())
    g = True
    for ing in ings:
        if ing not in prods:
            g = False
    if g: print(title)
