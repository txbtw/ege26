from sys import *
setrecursionlimit(10000)

def f(n):
    if n > 400:
        return n ** n
    if n <= 400:
        return n + 6 + f(n + 12)

print(f(72) - f(108))