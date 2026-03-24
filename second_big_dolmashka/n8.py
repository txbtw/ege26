from itertools import *
al = 'абиколун'
cnt = 0
for val in permutations(al, r=8):
    val = ''.join(val)
    for i in 'аиоу':
        val = val.replace(i, '*')
    for y in 'бклн':
        val = val.replace(y, '+')
    if '**' not in val and '++' not in val:
        cnt += 1
print(cnt)
