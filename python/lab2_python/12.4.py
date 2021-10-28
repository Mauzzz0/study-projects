def encode(inp):
    s = inp[0]
    c = 1
    for i in range(1, len(inp)):
        if inp[i] == s:
            c += 1
        else:
            break
    line = str(c) + " " + str(s)
    return line, inp[c:]


n = input()
while len(n) != 0:
    out, n = encode(n)
    print(out)
