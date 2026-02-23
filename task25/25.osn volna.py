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
    if len(d) == 2:
        prod(d)
    return d
from math import prod
cnt = 0
for i in range(1_324_727 + 1, 10**20):
    m = fact(i)
    if str(m).count('5') == 1:
        print(i, max(m))
        cnt += 1
        if cnt == 5:
            break
