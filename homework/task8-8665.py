from itertools import product
from string import printable
cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('b') == 2:
        for i in '13579b':
         val = val.replace(i, '*')
         for i in '02468a':
            val = val.replace(i, '+')
         if  val.count('11') == 2 and '**' not in val and '++' not in val:
            cnt += 1
print(cnt)
