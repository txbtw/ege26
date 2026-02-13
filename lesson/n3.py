from itertools import *
cnt = 0
for val in product('abcdef', repeat=6):
    val = ''.join(val)
    if 'a' not in val[0] and 'a' not in val[-1]:
        if 'e' not in val[0] and 'e' not in val[-1]:
            cnt += 1
print(cnt)