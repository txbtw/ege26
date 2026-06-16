def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(3, 1000):
    r = f(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r = f((n % 3) * 3, 3)
    r = int(r, 3)
    if r <= 150:
        print(n)
