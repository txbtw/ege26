from sys import *

setrecursionlimit(25000000)
def f(n):
    if n < 10: return 1
    else: return (n + 3) * f(n - 3)

print((f(247563)// 519 - 477 * f(247560)) // f(247557))
#1431