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
for i in range(6_651_220 + 1, 10**20):
    d = fact_3(i)
    if len(d) == 2 and str(d).count('2') == 1:
        print(i, d[-1])
        cnt += 1
        if cnt == 5:
            break