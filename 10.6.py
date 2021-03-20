seq = input()
symb, seq = seq[0], seq[1:]
pos = 1
line = symb
for s in seq:
    if s == ">":
        line += symb
        pos += 1
    elif s == "v":
        print(line)
        line = " " * (pos-1) + symb
    elif s == "<":
        pos -= 1
        line = line[::-1].replace(' ', symb, 1)[::-1]
print(line)
