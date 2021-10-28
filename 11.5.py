g = input()
for i in range(len(g)//2 + len(g)%2):
    print(g[i:-i])