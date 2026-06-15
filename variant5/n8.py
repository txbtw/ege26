from itertools import *
from string import *
cnt= 0
for val in product(printable[:7], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0246':
            val = val.replace(i, '*')
        if val.count('*') == 2:
            cnt += 1
print(cnt)