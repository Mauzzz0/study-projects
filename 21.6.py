import turtle
def tree(forward_len=200, minim_len=5):
    # Дерево представлено не как структура данных, а визуальною
    # Дерево будет строится бесконечно, пока длина конечной линии не станет 5
    # В данном случае максимальная глубина = 8
    # КОличество нод - 256
    # Перед вызовом tree() необходимо повернуть на 90 влево. "turtle.left(90)"
    turtle.forward(forward_len)  # Первая линия прямо, ствол текущей глубины текущего фрактала
    if forward_len > minim_len:
        # Прямой обход дерева
        turtle.left(45)
        tree(0.6*forward_len, minim_len)  # Рекурсивный вызов
        turtle.right(90)
        tree(0.6*forward_len, minim_len)
        turtle.left(45)  # Возврат напраления
    turtle.back(forward_len)


#  turtle.left(90)
#  tree()