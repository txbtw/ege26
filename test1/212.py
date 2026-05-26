from itertools import *

al = sorted('апрель')

for pos, val in enumerate(product(al, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in 'ал' and val.count('п') >= 2:
        print(pos)
        break