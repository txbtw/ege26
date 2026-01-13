from itertools import *
from string import *

cnt = 0
for val in product(printable[:14], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if len(set(val))  == 2:
            if val[-1] in '03':
                cnt += 1
print(cnt)