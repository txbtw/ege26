from itertools import *

al = sorted('аекнс')
for pos, val in enumerate(product(al, repeat=6), start=1):
    val = ''.join(val)
    if val == 'сенека':
        print(pos)