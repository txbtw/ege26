

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if d and max(d) % 7 == 0:
        return max(d)
    return 0


cnt = 0
for n in range(10**9 + 1, 10**20):
    if str(n) == str(n)[::-1] and (m := f(n)):
        print(n, m)
        cnt += 1
        if cnt == 5:
            break


