ll = [input() for _ in range(int(input()))]
print(len([x for x in ll if ll.count(x) > 1]))