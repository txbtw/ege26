def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d
cnt = 0
for i in range(3_333_338, 10**20):
    m = [x for x in f(i) if len(f(x)) == 0]
    r = max(m) - min(m)
    if r > 1000 and r % 3 == 0:
        print(i, r)
        cnt += 1
        if cnt == 5:
            break