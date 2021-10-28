import math


def roots_of_quadratic_equation(*kwargs):
    a = b = c = 0
    if len(kwargs) == 0 or len(kwargs) > 3:
        return None
    elif len(kwargs) == 2:
        b = kwargs[0]
        c = kwargs[1]
    elif len(kwargs) == 3:
        a = kwargs[0]
        b = kwargs[1]
        c = kwargs[2]
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return x1, x2
