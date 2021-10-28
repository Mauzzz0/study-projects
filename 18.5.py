def continue_continue_continue_making_sure_the_function_name_is_correct(a: str, b: str):
    x1 = float(a.split(";")[0])
    y1 = float(a.split(";")[1])
    x2 = float(b.split(";")[0])
    y2 = float(b.split(";")[1])
    try:
        k = (y1 - y2) / (x1 - x2)
    except:
        k = 0
    b = y2 - k * x2
    print(k, b)