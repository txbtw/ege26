def f(start, end):
    if start == end: return 1
    if start < end: return 0 # если в действиях вычти раздели итд
    return f(start- 2, end) + f(start // 2, end)

print(f(28, 10) * f(10, 1))
