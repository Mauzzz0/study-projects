def continueX9_making_sure_the_function_name_is_correct(digit: int) -> bool:
    # Function must RETURN
    if digit <= 1:
        return False
    if digit == 2:
        return True
    elif digit == 3:
        return True
    c = 0
    for i in range(1, digit//2 + 1):
        if (digit / i ) % 1 == 0:
            c += 1
    if c == 1:
        return True
    else:
        return False
