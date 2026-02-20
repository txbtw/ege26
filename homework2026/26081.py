def f(n):
    for x in range(113, i, 226):
        for n in range(0, 13):
            if x + 3 ** n == i:
                return n
    return 0



cnt = 0
for i in range(100000, 1000000, 2):
    if '0' not in str(i):
        if m := f(i):
            print(i, m)
            cnt += 1
            if cnt == 5:
                break



