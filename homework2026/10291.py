from itertools import *

cnt = 0
for val in set(permutations('джаваскрипт')):
    val = ''.join(val)
    summ = 0
    for i in range(len(val)):
        if val[i] in 'аи':
            summ += i + 1
    if summ == 11:
        cnt += 1
print(cnt)