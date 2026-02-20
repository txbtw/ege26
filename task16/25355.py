from functools import *

def f(n):
    if n >= 19:
        return f(n - 4) + 3580
    return 6*(g(n - 7) - 36)


@lru_cache(None)
def g(n):
    if n >= 248045:
        return n/20 + 28
    return g(n + 9) - 4

for i in range(250000, 0, -1):
    g(i)

print(f(673))