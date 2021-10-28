def continue_continue_continue_continue_continue_continue_continue_continue_making_sure_the_function_name_is_correct(inp: str) -> bool:
    # Function must RETURN values
    while " " in inp:
        inp = inp.replace(" ", "")
    inp = inp.lower()
    return inp == inp[::-1]
