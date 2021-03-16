_list = list()
for _ in range(int(input())):
    old_list = _list
    new_list = list()
    _list = list()
    for __ in range(int(input())):
        new_list.append(input())
    if _ == 0:
        _list = new_list
    else:
        for item in new_list:
            if item in old_list and _ != 0:
                _list.append(item)
print(*_list, sep="\n")
