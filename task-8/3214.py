from itertools import *
al = sorted('парус')
for pos, val in enumerate(product(al, repeat=5), start=1):
    val = ''.join(val)
    if val == 'уапап':
        print(pos)
