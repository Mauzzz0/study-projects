paths_access = [input() for _ in range(int(input()))]
paths_gets = [input() for _ in range(int(input()))]
for pth_g in paths_gets:
    res = "error"
    for pth_a in paths_access:
        if pth_a in pth_g:
            res = "success"
    print(res)