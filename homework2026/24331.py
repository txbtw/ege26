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
for i in range(13_475_125, 10**20):
    d = fact(i)
    if len(d) == 5 and all('5' in str(x) for x in set(d)):
        print(i, max(d))
        cnt += 1
        if cnt == 5:
            break