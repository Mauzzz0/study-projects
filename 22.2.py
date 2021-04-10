def partial_sums(*kwargs):
    res = [0]
    sm = 0
    for el in kwargs:
        sm += float(el)
        res.append(sm)
    return res