def f(x):
    return (x % a == 0) or (x % 133 == 0) <= (not(x % 95 == 0))
for a in range(1, 10000)[::-1]:
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break