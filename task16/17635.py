from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * f(n - 1)

for i in range(0, 2025):
    f(i)

print((f(2024) - 3 * f(2023)) / f(2022))
