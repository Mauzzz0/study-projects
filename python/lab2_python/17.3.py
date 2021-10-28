dic = dict({
    "янв": [],
    "фев": [],
    "мар": [],
    "июн": [],
    "июл": [],
    "авг": [],
    "сен": [],
    "окт": [],
    "ноя": [],
    "дек": []
})

for _ in range(int(input())):
    inp = input()
    g1 = "".join([x for x in inp.split(' ')[:2]])
    g2 = inp.split(' ')[2]
    ar = dic[g2]
    ar.append(g1)
    dic[g2] = ar
for _ in range(int(input())):
    print(*dic[input()], sep=" ")

