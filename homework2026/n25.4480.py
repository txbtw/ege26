def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if (sum(d) and len(d) % 2) != 0:
        return d
    return 0
cnt = 0
for n in range(800_001, 10**20):
    m = f(n)
    if m > 10:
        print(n, m)
        cnt += 1
        if cnt == 6:
            break




