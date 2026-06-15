from math import *

for n in range(1, 10**5)[::-1]:
    l = 257
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 295_740 <= 33 * 2 **20:
        print(n)
        break