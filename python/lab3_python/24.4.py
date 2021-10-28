lst = [input().lower() for x in range(int(input()))]
done = list()
for i in range(len(lst)):
    item_list = sorted(list((lst[i])))
    done.append(lst[i])
    print(lst[i], end=" ")
    for j in range(i, len(lst)):
        if sorted(list((lst[j]))) == item_list and lst[j] not in done:
            done.append(lst[j])
            print(lst[j],end =" ")
    print()
