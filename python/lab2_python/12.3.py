arr = list()
for _ in range(int(input())):
    arr.append([input(), input()])
for item in reversed(arr):
    print(*item, sep=" ")
