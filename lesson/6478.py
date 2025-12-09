from itertools import *
cnt = 0
for val in product('моль', repeat=6):
    val = ''.join(val)
    if 