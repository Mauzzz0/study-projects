old = list()
def print_only_new(message: str):
    global old
    if message not in old:
        old.append(message)
        print(message)
