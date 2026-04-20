def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    for i in sorted(d):
        if i % 100 == 11 and i != 11:
            return i
    return 0

cnt = 0
for n in range(1_350_050 + 1, 10**20):
    if x := f(n):
        print(n, x)
        cnt += 1
        if cnt == 5:
            break