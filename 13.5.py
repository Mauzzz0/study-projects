arr = list()
for _ in range(int(input())):
    b = input()
    a = int(input())
    arr.append([a, b])
b = list(reversed(sorted(arr)))
for item in reversed(sorted(arr)):
    print(item[0])
