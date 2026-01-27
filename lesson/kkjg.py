

from itertools import *
from string import *
cnt = 0
for val in product(printable[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 1 and (i + i not in val for i in printable[:16]):
        cnt += 1
print(cnt)