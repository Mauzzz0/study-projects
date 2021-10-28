from random import randint
def score(point, p=0):
    res = None
    internal = dict()
    external = dict()
    for i in range(1,21):
        internal[str(i)] = randint(1, 50)
        external[str(i)] = randint(1, 50)
    if point == "яблочко":
        res = 50
    elif point == "зел кольцо":
        res = 25
    elif point == "внешнее":
        res = external[str(p)]
    elif point == "внутреннее":
        res = internal[str(p)]
    return res
