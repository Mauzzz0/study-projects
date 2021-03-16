for _ in range(int(input())):
    line = input()
    if line[0:2] == "%%":
        print(line[2:])
    elif line[0:4] == "####":
        pass
    else:
        print(line)