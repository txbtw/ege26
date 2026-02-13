def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d
# [x for x in f(i) if len(f(x)) == 0]
cnt = 0
for i in range(3_333_338, 10**20):
    m = []
    for x in f(i): # [x for x in f(i) if len(f(x)) == 0] второй способ черзе генератор
        if len(f(x)) == 0:
            m += [x]
    r = max(m) - min(m)
    if r > 1000 and r % 3 == 0:
        print(i, r)
        cnt += 1
        if cnt == 5:
            break