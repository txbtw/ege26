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

    if num > 2:
        d += [num]

    return d
cnt = 0
for i in range(1_324_727 + 1, 10**20):
    m = fact(i)
    if  len(m) == 2 and all(str(x).count('5') == 1 for x in m):
        print(i, max(m))
        cnt += 1
        if cnt == 5:
            break
