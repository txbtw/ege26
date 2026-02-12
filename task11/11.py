from math import *

for L in range(1, 10 ** 9):
    N = 2051
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 836 * I <= 639 * 2 **10:
        print(L)

