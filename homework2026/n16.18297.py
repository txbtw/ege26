from sys import *
setrecursionlimit(10000)
def f(n):
    if n < 10:
        return n - 1
    if n >= 10 and n % 2 == 0:
        return 3* n - 1 + f(n - 3)
    if n >= 10 and n % 2 != 0:
        return 5 * n + 2 + f(n- 4)

print(f(4445) - f(4444))