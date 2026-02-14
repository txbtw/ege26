

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if str(d) == str(d)[::-1]:
        return max(d)
    return 0
cnt = 0
for i in range(10**9 + 1, 10**20):
    m = f(i)
    if m % 7 == 0:
        print(i, m)
        cnt += 1
        if cnt == 5:
            break