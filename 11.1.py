g = input()
s = 0
mx = -10
prev = None
for symb in g:
    if prev == None:
        prev = symb
        s = 1
        continue
    if prev == "о" and symb == "о":
        s += 1
    else:
        if s > mx:
            mx = s
            s = 0
            prev = None
print(mx-1)