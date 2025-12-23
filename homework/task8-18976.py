from itertools import *
from string import *
cnt = 0
for val in product(printable[:20], repeat=5):
    val = ''.join(val)
    for i in printable[:20]:
        if i % 2 == 0:
            val = val.replace(i, '*')
        else:
            val = val.replace(i, '+')
    if '*+' in val and '+*' in val and val[0] + val[-1] == 26:
        cnt += 1
print(cnt)