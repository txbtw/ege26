def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}
    for i in sorted(d):
        if i != 0 and i % 17 == 0:
            return i
    return 0
cnt = 0
for i in range(250_000 + 1, 10**20):
    if s := f(i):
        print(i, s)
        cnt += 1
        if cnt == 5:
            break


