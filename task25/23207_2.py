def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 1:
        d += [num]

    return d

cnt = 0
for i in range(1_324_728, 10**10):
    if m := fact(i):
        if len(m) == 2:
            if sum(str(x).count('5') == 1 for x in m) == 2:
                print(i, max(m))
                cnt += 1
                if cnt == 5:
                    break