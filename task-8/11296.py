from itertools import product
al = sorted('досж')
for pos, val in enumerate(product(al, repeat=6), start=1):
    val = ''.join(val)
    if 

