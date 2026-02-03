from itertools import *
cnt = 0
for val in product('м*сл*', repeat=6):
    val = ''.join(val)
    if val.count('*') == 1:
        cnt += 1
print(cnt)