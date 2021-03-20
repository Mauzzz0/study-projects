lst = list()
for _ in range(int(input())):
    """
    Ivanov came
    Kyznetsov came
    Polivanov came
    Zorina over Kyznetsov
    Ivanova gone
    """
    g = input().split(" ")
    if len(g) == 2:
        if g[1] == "came":
            lst.append(g[0])
        elif g[1] == 'gone':
            lst.remove(g[0])
    elif len(g) == 3:
        lst.insert(lst.index(g[2])+1, g[0])
for j in lst:
    print(j)
