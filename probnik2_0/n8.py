from itertools import *

al = sorted('строка')

for pos, val in enumerate(product(al, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in  'ал' and val.count('с') == 1:
        print(pos)