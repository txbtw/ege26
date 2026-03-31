def f(s, e):
    if s == e: return 1
    if s < e or s == 18: return 0
    return f(s- 3, e) + f(s- 5, e) + f(s// 3, e)
res1 = f(80, 38) * f(38, 3)

def f1(s, e):
    if s == e: return 1
    if s < e or s == 38: return 0
    return f(s- 3, e) + f(s- 5, e) + f(s// 3, e)
res2 = f(80, 18) * f(18, 3)
print(res2 + res1)