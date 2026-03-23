def isprime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            if isprime(i): d |= {i}
            if isprime(num // i): d |= {num // i}
    return min(d) + max(d)
cnt = 0
for i in range(23_600_000,10**20):
    m = f(i)
    if m % 213 == 171:
        print(i, m)
        cnt += 1
        if cnt == 6:
            break