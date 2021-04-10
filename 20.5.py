lastTicket = None
def lucky(ticket: str):
    # Function must RETURN result
    global lastTicket
    lst = str(lastTicket)
    sum1 = int(lst[0]) + int(lst[1]) + int(lst[2])
    sum2 = int(lst[3]) + int(lst[4]) + int(lst[5])
    sum3 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum4 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if sum1 == sum2 and sum3 == sum4:
        return True
    return False