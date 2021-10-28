thimbles = list()
for _ in range(int(input())):
    thimbles.append(input())
for per in range(int(input())):
    c = int(input())
    tmp_arr = list()
    for _ in range(c):
        tmp_arr.append(thimbles[int(input())-1])
    thimbles = tmp_arr
print(*thimbles, sep="\n")