from itertools import *
al = sorted('аожпюз')
cnt = 0
for pos,val in enumerate(product(al, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'а' and val.count('з') >= 2:
        cnt += 1
print(cnt)