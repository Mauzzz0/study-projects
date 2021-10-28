n = int(input())
m = int(input())
books = list()
for _ in range(n):
    books.append(input())
for _ in range(m):
    print("YES" if input() in books else "NO")