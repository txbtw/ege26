def f(x):
    return (not((x,11,18) == (not(max(x, 5) > 68)))) and (x, a, 5)

for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break