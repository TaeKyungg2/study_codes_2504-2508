def eratos(n, k):
    num = 2
    multi = 1
    del_num = set()
    num_change = 2
    count = 0
    while True:
        num_change = num * multi
        if num_change in del_num:
            if multi == 1:
                num += 1
                num_change = num
                continue
            multi += 1
            continue
        if num_change > n:
            multi = 1
            num += 1
            num_change = num
            continue
        del_num.add(num_change)
        count += 1
        multi += 1
        if count == k:
            print(num_change)
            break


n, k = map(int, input().split())
eratos(n, k)
