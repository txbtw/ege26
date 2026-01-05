from string import *
from itertools import *
cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != 0 and val[0] % 2 != 1 and val[-1] % 3 != 0 and val.count('6') >= 1:
        cnt += 1
print(cnt)