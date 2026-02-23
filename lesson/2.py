from itertools import *
cnt = 0
for val in product('012345678', repeat=7):
    val = ''.join(val)
    if val[0] != '0' and '2' not in val:
        if len(set(val)) == len(val):
            for i in '012345678':
                if int(i, 9) % 2 == 0:
                    val = val.replace(i, '*')
                else:
                    val = val.replace(i, '+')
            if '**' not in val and '++' not in val:
                cnt += 1
print(cnt)
