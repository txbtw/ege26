from itertools import *
cnt = 0
for val in permutations('амфибрахий'):
    val = ''.join(val)
    if 'иифаа' in val and 'аафии' in val:
        cnt += 1
print(cnt)