from math import *

for n in range(1, 10**9):
    l = 377
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 23155 > 5536 * 2 **10:
        print(n)
        break

for l in range(1, 10**10):
    n = 10 + 17
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 7_564_230 > 31 * 2 ** 20:
        print(l)
        break