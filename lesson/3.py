from itertools import *
from  string import *

cnt = 0
for val in product(printable[:16], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 2:
        for i in val:
            if int(i, 16) % 2 == 0:
                    val = val.replace('6', '+')
                    val = val.replace(i, '*')
        if '*+' not in val and '+*' not in val and '++' not in val:
            cnt += 1
print(cnt)


