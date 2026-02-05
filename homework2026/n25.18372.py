def f(num):
    d = {1}
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return sum(d) // len(d)

cnt = 0
for n in range(1, 770000)[::-1]:
    m = f(n)
    if m % 100 == 12:
        print(n, m)
        cnt += 1
        if cnt == 5:
            break