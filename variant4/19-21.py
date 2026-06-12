def f(x, c, s):
    if x + c >= 77: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 3, c, s - 1), f(x * 3, c , s - 1), f(x, c + 3, s - 1), f(x, c * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19burmalda', [c for c in range(1 ,65) if f(12, c, 2)])
print('20burmalda', [c for c in range(1 ,65) if f(12, c, 3) and not f(12, c, 1)])
print('20burmalda', [c for c in range(1 ,65) if f(12, c, 4) and not f(12, c, 2)])