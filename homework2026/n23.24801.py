from functools import lru_cache

@lru_cache(None)
def f(start, end, flag24, flag32):
    if start == 24: flag24 = True
    if start == 32: flag32 = True
    if start == end and flag24 + flag32 == 1: return 1
    if start > end or flag24 + flag32 == 2: return 0
    return f(start + 1, end, flag24, flag32) + \
        f(start + 2, end, flag24, flag32) + \
        f(start + 4, end, flag24, flag32) + \
        f(start + 8, end, flag24, flag32)


print(f(16,48, False, False))

#################################################################
def f1(start, end):
    if start == end: return 1
    if start > end or start == 24: return 0
    return f1(start + 1, end) + f1(start + 2, end) + f1(start + 4, end) + f1(start + 8, end)
res1 = f1(16, 32) * f1(32, 48)

def f(start, end):
    if start == end: return 1
    if start > end or start == 32: return 0
    return f(start + 1, end) + f(start + 2, end) + f(start + 4, end) + f(start + 8, end)
res = f(16, 24) * f(24, 48)
print(res1 + res)