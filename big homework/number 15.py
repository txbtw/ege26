def f(x):
    return (x % 17 == 0) <= (not(80 <= x <= 100) or (a < x + 30))

for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break