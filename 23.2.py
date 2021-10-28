from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    tuple_max = None
    max_s = 0
    for a, b in orbits:
        if a*b*pi > max_s and a != b:
            max_s = a*b*pi
            tuple_max = (a, b)
    return tuple_max

print(*find_farthest_orbit(orbits))
