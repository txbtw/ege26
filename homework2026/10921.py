from itertools import *

cnt = 0

for val in set(permutations('джаваскрипт')):
    val = ''.join(val)
    if val.count('а') == 1 and val.count('и') == 1:
        cnt += 1

print(cnt)
