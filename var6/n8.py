from itertools import *
al = sorted('аргумент')

for pos, val in enumerate(product(al, repeat=4), start=1):
    val = ''.join(val)
    if len(set(val)) == len(val):
        print(pos)
