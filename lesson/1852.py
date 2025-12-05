from itertools import product
cnt = 0
for val in product('гепард', repeat=5 ):
    val = ''.join(val)
    if val.count('г') == 1 and val[0] != 'а' and val[-1] != 'е':
        cnt += 1
print(cnt)

