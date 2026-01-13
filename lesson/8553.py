from itertools import *
cnt = -1
for pos, val in enumerate(product(sorted('нормалье'), repeat=6), start=1):
    val = ''.join(val)
    if val[:4] == 'норм':
        cnt += 1
    if val[:6] == 'ненорм':


print(cnt)
