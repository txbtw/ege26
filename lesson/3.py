from itertools import *

cnt = 0
for val in permutations('х*ч*н*б*дж*т'):
    val = ''.join(val)
    if '*****' not in val:
        cnt += 1
print(cnt)

