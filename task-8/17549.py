from itertools import *
alp = sorted('фокус')

for pos, val in enumerate(product(alp, repeat=5), start=1):
    val = ''.join(val)
    if 'ф' not in val and val.count('у') == 2:
        print(pos)
