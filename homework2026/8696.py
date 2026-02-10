def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) == 0:
        return 0
    m = sum(d)
    if isprime(m % 100000):
        return m
    return 0

def isprime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

cnt = 0
for n in range(1_273_547, 10**20):
    if i := f(n):
        print(n, i)
        cnt += 1
        if cnt  == 5:
            break