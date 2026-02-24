from itertools import *

cnt = 0

for val in set(permutations('просто')):
    val = ''.join(val)
    if all(x + x not in val for x in val):
        cnt += 1

print(cnt)