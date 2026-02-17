from functools import *
from sys import *

@lru_cache(None)
def f(n):
    if n < 3:
        return 3
    else:
        return 2 * n + 5 + f(n - 2)

for i in range()


print(f(3027) - f(3023))
