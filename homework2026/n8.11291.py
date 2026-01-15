from itertools import *
cnt = 0
for val in product('012345', repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('2') == 1:
        val = val.replace('0', '*').replace('4', '*')
        if '*2' not in val and '2*' not in val and '22':
            cnt += 1
print(cnt)