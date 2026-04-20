from itertools import *
al = sorted('символ')
for pos, val in enumerate(product(al, repeat=5), start=1):
    if val[0] not in 'ос' and val.count('в') == 1 and val.count('с') <= 1:
        if pos % 2 != 0:
            print(pos)