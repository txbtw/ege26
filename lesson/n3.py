from itertools import *
cnt = 0
al = '*+*+ '
for val in product(al, repeat=5):
    val = ''.join(val)
    if '++' not in val and '**' not in val:
        if val.count(' ') == 1 and ' ' not in val[0] and ' ' not in val[-1]:
            cnt += 1
print(cnt)