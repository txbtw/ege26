from itertools import *
from string import *

cnt = 0
for val in product(printable[:9], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('0') == 1:
            for i in '1357':
                val = val.replace(i, '*')
            if '*0' not in val and '0*' not in val:
                cnt += 1
print(cnt)