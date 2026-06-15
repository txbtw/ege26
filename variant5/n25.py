def isprime(num):
    if num <2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if isprime(i): d |= {i}
            if isprime(num // i): d |= {num // i}
    return d






cnt = 0
for i in range(7_800_000 + 1, 10**10):
    if M := f(i):
        m = min(M) + max(M)
        if m % 100 == 63 and m % (len(M)) == 0:
            print(i, m)
            cnt += 1
            if cnt == 5:
                break