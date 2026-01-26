def f(x, y):
    return (x + y <= 30) or (y <= x + 2) or (y >= a)
for a in range(0, 1000)[::-1]:
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
