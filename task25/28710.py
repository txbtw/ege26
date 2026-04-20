def fact_3(num):
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
for n in range(3_600_001, 10**20):
    m = fact_3(n)
    if len(m) == 3 and all('3' in str(i) and '5' in str(i) for i in m):
        print(n, max(m))
        cnt += 1
        if cnt == 5:
            break
