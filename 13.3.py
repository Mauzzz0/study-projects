lst = "0"
for _ in range(int(input())-1):
    c = 0
    for i in range(len(lst)):
        if lst[i] == lst[::-1][i]:
            c += 1
    lst += str(c)
print(lst)
