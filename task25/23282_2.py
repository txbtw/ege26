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
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 1:
        d += [num]

    return d

def f(num):
    d = set()
    for i in range(2, int(num ** .5)):
        if num % i == 0:
            if isprime(i): d |= {i}
            if isprime(num // i): d |= {num // i}
    if len(d) > 1:
        return min(d) + max(d)

cnt = 0
for i in range(5_400_001, 10**20):
    if M := f(i):
        if M > 60000 and str(M) == str(M)[::-1]:
            print(i, M)
            cnt += 1
            if cnt == 5:
                break