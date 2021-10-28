arr = list()
for _ in range(int(input())):
    arr.append(input())
g = int(input())
while len(arr) != 0 :
    pops = list()
    for i in range(len(arr)):
        if i%g == 0:
            print(arr[i])
            pops.append(arr[i])
    for el in pops:
        arr.remove(el)