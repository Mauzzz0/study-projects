inp = input().split('\n')
res = False
for el in inp:
    el = el.split(' ')
    if "0" in el:
        res = True
        break
print(res)