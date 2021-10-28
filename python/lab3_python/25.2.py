from random import randint
def generate_password(count, length):
    storage = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    output = list()
    while len(output) != count:
        random_indexes = list()
        prev = None
        to_output = ""
        while len(random_indexes) != length:
            rnd = randint(0, len(storage)-1)
            if rnd != prev:
                random_indexes.append(rnd)
                prev = rnd
        for i in range(len(random_indexes)):
            if i == 0:
                to_output += "5"
            elif i == 1:
                to_output += storage[random_indexes[i]].upper()
            else:
                to_output += storage[random_indexes[i]]
        output.append(to_output)
    return output


print(*generate_password(10, 15), sep="\n")