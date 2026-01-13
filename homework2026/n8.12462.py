from itertools import product
from string import printable
cnt1 = 0
cnt2 = 0
for val in product(printable[:16], repeat=3):
    val = ''.join(val)
    if val[0] != '0':
        if