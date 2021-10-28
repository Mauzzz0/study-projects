def continue_continue_making_sure_the_function_name_is_correct(string: str):
    res = ""
    opnd = 0
    t = [x for x in string]
    if t[0] == ")" or t[-1] == "(":
        res = "NO"
        return res
    for b in t:
        if b == "(":
            opnd += 1
        elif b == ")":
            opnd -= 1
        else:
            res = "error"
            return res
    if opnd == 0 and res != "error":
        res = "YES"
    print(res)