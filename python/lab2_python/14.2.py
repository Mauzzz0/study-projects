"""
To: ivanov
Сергей Иванов, ваш пароль слишком простой, смените
его.
To: polivanov
Андрей Поливанов, ваш пароль слишком простой,
смените его.
"""
arr = list()
inp = input()
while inp != '':
    inp = inp.split(':')
    arr.append([inp[0], inp[1], inp[4].split(',')[0]])
    inp = input()

psswrds = input().split(';')
for g in arr:
    if g[1] in psswrds:
        print("to", g[0])
        print(g[2],"change your password")