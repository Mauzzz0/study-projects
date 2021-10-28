values = [0, 2, 10, 6]

def same_by(characteristic, objects):
    g = set(map(characteristic, objects))
    gl = len(g)
    return gl == 1

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
