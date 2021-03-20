n = int(input())
m = int(input())
out = "\n"
for j in range(n):
    inp = input()
    if j % 2 == 0:
        for i in range(0, len(inp), 2):
            out += inp[i]
        out += "\n"
print(out)
