from itertools import *
cnt = 0
for val in product('01', repeat=16):
    val = ''.join(val)
    if val[0] != '0' and val.count('1') % 3 == 0:
        cnt += 1
print(cnt)
