dic = dict()
ch = dict()
for _ in range(int(input())):
    """Name repostname views
    Name views
5
YA 15
Ivan YA 40
Vas YA 13
OP YA 39
PJ OP 21
    """
    inp = input().split(" ")
    if len(inp) == 2:
        dic[inp[0]] = int(inp[1])
    else:
        dic[inp[0]] = int(inp[2])
        dic[inp[1]] = dic[inp[1]] + int(inp[2])
        parent = inp[0]
        child = inp[1]
        views = int(inp[2])
        ch[parent] = child
        while child in ch.keys():
            dic[child] = dic[child] + views
            try:
                child = dic[child]
            except:
                break

for key, val in dic.items():
    print(key, val)