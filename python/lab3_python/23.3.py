inp = input().split(' ')
d = ['а', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
c = 0
closed = False
for el in inp:
    _c = 0
    for e in el:
        if e in d:
            _c += 1
    if c == 0:
        c = _c
    else:
        if c != _c:
            print('error')
            closed = True

if not closed:
    print('success')