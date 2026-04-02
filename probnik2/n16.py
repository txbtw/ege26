from sys import setrecursionlimit


setrecursionlimit(15000)
def f(n):
    return 3 * (g(n - 2) + 5)

def g(n):
    if n < 8: return 3* n
    return g(n - 3) + 2

print(f(12345))