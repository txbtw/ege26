from itertools import *

al = sorted('апрель')

for pos, val in enumerate(product(al, repeat=6)):
    val = ''.join(val)
    if (val[0] != 'а' or val[0] != 'л') and val.count('п') >= 2 and pos % 2 != 0:
        print(pos)
        break
# 21