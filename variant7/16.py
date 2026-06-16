from sys import *
setrecursionlimit(35000)

def f(n):
    if n < 31054: return f(n + 4) + 3020
    return 3 * (g(n - 2) - 15)

def g(n):
    if n >= 28: return g(n - 5) - 15
    return 3 * n - 4

print(f(15))