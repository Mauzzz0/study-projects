prods = [input() for _ in range(int(input()))]
for _ in range(int(input())):
    for __ in range(int(input())):
        try: prods.remove(input())
        except: None
print(*prods, sep="\n")