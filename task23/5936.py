def f(start, end):
    x = []
    for i in range(1, 626):
        if i % 2 == 0:
            x.append(i)
    if start == end or start == x and len(x) <= 4: return 1
    if start > end: return 0
    return f(start + 2, end) + f(start + 3, end) + f(start * 2 + 1, end)

print(f(1, 625))