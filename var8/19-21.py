def f(x, c, s):
    if x + c >= 227: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x + 1, c , s -1),
        f(x * 2, c , s - 1),
        f(x, c + 1, s - 1),
        f(x, c * 2, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)))' ,[c for c in range(1, 210) if f(17, c, 2)])
print('19)))' ,[c for c in range(1, 210) if f(17, c, 3) and not f(17, c, 1)])
print('19)))' ,[c for c in range(1, 210) if f(17, c, 4) and not f(17, c, 2)])