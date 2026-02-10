def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d
print(f(10))
def isprime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

cnt = 0
for n in range(1_273_547, 10**20):
    m = f(n)
    if m % 100 == isprime():
        print(n, m)
        cnt += 1
        if cnt  == 5:
            break