from string import *
from itertools import *

cnt = 0
for val in permutations(printable[:10], r=4):
    val = ''.join(val)
    if val[0] != '0':
        for i in printable[:10]:
            if int(i, 10) % 2 == 0:
                val = val.replace(i, '*')
            else:
                val = val.replace(i, '+')
        if '**' not in val and '++' not in val:
            cnt += 1
print(cnt)