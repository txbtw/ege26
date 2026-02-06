def isprime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i * i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d

cnt = 0
for n in range(89428305, 10**20):
    d = fact(n)
    if len(d) == 6 and isprime(d):
        print(n, d)
        cnt += 1
        if cnt == 6:
            break
