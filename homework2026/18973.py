from string import *
from itertools import *

cnt = 0
for val in product(printable[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        for i in val:
            if int(i) > 15:
                for x in val:
                    if int(x) % 2:
                        val = val.replace(x, '*')
                if val.count('*') >= 1:
                    cnt += 1
print(cnt)