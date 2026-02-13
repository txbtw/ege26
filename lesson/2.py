def f(x, y):
    return not((x < 7) or (y >= 5 * x + a - 60) or (x >= 36) or (y < 225))

for a in range(0, 1000)[::-1]:
    if all(not f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break
