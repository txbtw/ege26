from itertools import *
cnt = 0
for val in set(permutations('кидала', r=5)):
    val = ''.join(val)
    if  'кк' not in val and 'ии' not in val and 'дд' not in val and 'аа' not in val and 'лл'  not in val:
        cnt += 1
print(cnt)