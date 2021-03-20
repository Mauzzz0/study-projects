digs = [int(x) for x in input().split(' ')]
print("*"*(len(digs)+2)+"\n*"+" "*len(digs)+"*")
for i in range(max(digs), 0, -1):
    line = "*"
    for dig in digs:
        if dig >= i:
            line += "*"
        else:
            line += " "
    line += "*"
    print(line)
