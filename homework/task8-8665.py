from itertools import product
from string import printable
cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    for i in '13579b':
        val = val.replace(i, '*')
    for i in '02468a':
        val = val.replace(i, '+')

    if val[0] != '0' and val.count('11') == 2 and '*+*+*+*+*+*+' in val and '+*+*+*+*+*+*' in val:
        cnt += 1
print(cnt)
