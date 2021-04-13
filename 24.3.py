g = input()
c = 1
while g:
    try:
        print('Line '+str(c)+": "+g.split('#')[1])
    except IndexError: pass
    g = input()
    c += 1
