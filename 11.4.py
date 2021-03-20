for _ in range(int(input())):
    inp = input()
    line = ""
    inside_quotes = False
    is_started = False
    previous = None
    for i in range(len(inp)):
        if inp[i] == " " and is_started == False:
            line += ' '
        elif inp[i] == " " and is_started == True and previous != ' ':
            line += ' '
        elif inp[i] == ' ' and is_started == True and previous == ' ':
            continue
        else:
            is_started = True
            if inp[i] == "'":
                inside_quotes = not inside_quotes
                line += "'"
            elif inp[i] == '#' and not inside_quotes:
                break
            elif inp[i] == '#' and inside_quotes:
                line += '#'
            else:
                line += inp[i]
        previous = inp[i]
    """
    inp = inp.split('#')[0] if not inp.find("'") < inp.find('#') < inp.rfind("'") else inp
    prefix = ""
    while " " == inp[0]:
        prefix += " "
        inp = inp[1:]
    while "  " in inp and inp.find("'") < inp.find('  ') < inp.rfind("'"):
        inp = inp.replace('  ', ' ')
    """
    print(line)
