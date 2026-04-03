from itertools import *
from string import *

cnt = 0
for val in product(printable[:7], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val[0] not in '35' and ('22' not in val) and ('44' not in val):
            cnt += 1
print(cnt)