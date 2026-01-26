from sys import *
setrecursionlimit(350000)

def f(n):
    if n > 40:
        return f(n-4) + 3020
    if n <= 40:
        return 3 * (g(n - 2) - 15)
def g(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return g(n+7) - 21
print(f(2026))