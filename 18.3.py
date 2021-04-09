def continue_making_sure_the_function_name_is_correct(n: int):
    n -= 1
    i = 0
    prev_fib1 = prev_fib2 = 0
    fib1 = fib2 = 1
    while n > 0:
        prev_fib1 = fib1
        prev_fib2 = fib2
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    print(fib2/fib1)