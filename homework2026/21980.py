def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d
cnt = 0
for p in range(750000 - 1, 0, -1 ):
    m = f(p)
    prost = []
    for x in m:
        if len(f(x)) == 0 and x %10 == 7:
            prost.append(x)
    if len(prost):
        f = sum(prost) // len(prost)
    else:
        f =0
    if f != 0 and f % 111 == 0:
        print(p, f)
        cnt += 1
        if cnt == 5:
            break