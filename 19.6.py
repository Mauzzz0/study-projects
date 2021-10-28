def continueX10_making_sure_the_function_name_is_correct(n: int):
    # Function must RETURN values
    if n >= 2:
        c = ((2 * ((2 * n) - 1)) / (n + 1)) * continueX10_making_sure_the_function_name_is_correct(n - 1)
        return int(c)
    return 1