from itertools import *
al = sorted('автор')
cnt = 0
for pos, val in enumerate(product(al, repeat=4), start=1):
    val = ''.join(val)
    if val == 'вата':
        print(pos)
