from itertools import *
cnt = 0
for val in product('алгоритм', repeat=6):
    if val.count('л') == 1 or 'л' not in val and val[0] != 'р' and val[-1] != 'лгртм':
        cnt += 1
print(cnt)