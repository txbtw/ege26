from itertools import product
al = sorted('январь')

for pos, val in enumerate(product(al, repeat=5), start=1):
    val = ''.join(val)
    if val == 'ьяряр':
        print(pos)