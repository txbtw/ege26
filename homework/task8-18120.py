from itertools import *
al = sorted('ссессос')
cnt = 0
for pos, val  in enumerate(product(al, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[-1] in 'ео'  and val.count('с') <= 3:
        cnt += 1
print(cnt)