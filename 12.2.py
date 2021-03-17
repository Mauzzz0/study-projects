inp = input()
while '  ' in inp:
    inp = inp.replace('  ', ' ')
g, sm = inp.split(' ')
_sm = 0
for _ in range(int(g)):
    line = input()
    while ' ' in line:
        line = line.replace(' ','')
    _1 = int(line.split('*')[0])
    _2 = int(line.split('*')[1].split('=')[0])
    _3 = int(line.split('*')[1].split('=')[1])
    _sm += _1*_2
    if _1 * _2 != _3:
        print(_+1)
print('delta:', abs(_sm-int(sm)))
