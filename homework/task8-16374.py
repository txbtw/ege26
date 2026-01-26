from itertools import *

cnt = 0
for val in product('0123456', repeat=7):
    val = ''.join(val)
    for i in '0123456':
        if int(i, 7) % 2 == 0:
            val = val.replace(i, '*')
    if val[0] != '0' and  val.count('*') == 2:
        cnt += 1

print(cnt)