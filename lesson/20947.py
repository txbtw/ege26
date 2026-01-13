from itertools import *
cnt =0
for val in permutations('кайф'):
    val = ''.join(val)
    if val[-1] != 'й' and 'кф' not in val:
        cnt += 1
print(cnt)

