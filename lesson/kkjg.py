from itertools import product
al = sorted('школа')
for pos, val in enumerate(product(al, repeat=5), start=1):
    val = ''.join(val)
    if val == 'шалаш':
        print(pos)