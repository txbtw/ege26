from string import *
from itertools import *
cnt = 0
for val in product(printable[:8], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == len(val) and '1' not in val:
        for i in printable[:8]:
            if int(i, 8) % 2 == 0:
                val = val.replace(i, '*')
            else:
                val = val.replace(i, '+')
        if '**' not in val and '++' not in val:
            cnt += 1
print(cnt)
h