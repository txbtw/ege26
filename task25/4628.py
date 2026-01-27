from fnmatch import *
for n in range(124065 - 1234065 % 161, 10**8 + 1, 161):
    if fnmatch(str(n), '12*4?65'):
        print(n, n // 161)

ans = []
from string import *
from itertools import *
for v in printable[:10]:
    for l in range(0, 3):
        for z in product(printable[:10], repeat=l):
            num = int(f'12{''.join(z)}4{v}65')
            if num % 161 == 0 and num <= 10**8:
                ans.append([num, num // 161])
for i in sorted(ans):
    print(*i)
