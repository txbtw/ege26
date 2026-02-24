def f(num):
    d = set()
    for i in range(2, int(num ** .5)+1):
        if num % i == 0:
            d |= {i, num // i}
    return d
cnt = 0
for i in range(456789 + 1, 10**20):
    p = f(i)
    prost = []
    for x in p:
        if len(f(x)) == 0:
            prost.append(x)
    if len(prost) >= 4:
        m = prost[0] + prost[1] + prost[-1] + prost[-2]
        if m % 114 == 39:
            print(i, m)
            cnt += 1
            if cnt == 5:
                break





