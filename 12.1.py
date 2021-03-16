white = list()
for _ in range(int(input())):
    white.append(input())
for _ in range(int(input())):
    g = input()
    if g in white:
        print(g)