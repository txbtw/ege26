def f(start, end):
    if start == end: return 1
    if start > end or start in {24, 32}: return 0
    return f(start + 1, end) + f(start + 2, end) + f(start + 4, end) + f(start + 8,end)

print(f(16, 48))