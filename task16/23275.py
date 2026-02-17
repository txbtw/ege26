from functools import *
@lru_cache(None)
def f(n):
    return 2* (g(n - 3) + 8)
for i in range(0, 16000):
    f(i)

@lru_cache(None)
def g(n):
    if n < 10:
        return 2* n
    else:
        return g(n - 2) + 1
for i in range(0, 16000):
    g(i)

print(f(15548))
