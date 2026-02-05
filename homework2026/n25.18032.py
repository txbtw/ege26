def f(num):
    i = 0
    for d in range(1, num + 1):
        if num % d == 0:
             i += d
    return i








for n in range(1000, 10000):
    m = f(n)
    if m % 100 == 23:
        print(n, m)