from math import *

for n in range(1, 10**9):
    l = 377
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 23155 > 5536 * 2 **10:
        print(n)
        break
print(int('1111000', 2))