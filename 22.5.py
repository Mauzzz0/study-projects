def solve(*kaefi):
    roots = []
    lenght = len(kaefi)
    if lenght == 1:
        if kaefi[0] == 0:
            roots.append('all')
    if len(kaefi) == 2:
        b, c = kaefi[0], kaefi[1]
        roots.append(-c / b)
        print(*roots)
    if lenght == 3:
        a = kaefi[0]
        b = kaefi[1]
        c = kaefi[2]
        disc = b ** 2 - 4 * a * c
        if disc == 0:
            roots.append(-b / 2 * a)
        elif disc > 0:
            x1 = (-b + disc**0.5) / (a + a)
            x2 = (-b - disc**0.5) / (a + a)
            roots.append(x1)
            roots.append(x2)
    print(*roots)