def making_sure_the_function_name_is_correct():
    res = "denied"
    for _ in range(3):
        if input() == "password":
            res = "allowed"
            print(res)
            return
    print(res)
    return

