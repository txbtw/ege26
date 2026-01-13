from string import *
from itertools import *
cnt = 0
for val in product(printable[:25], repeat=4):
    if val[0] != '0':
        for i in printable[:25]:
            if int(i, 25) % 2 != 0:
                i = i.replace(i, '+')
        if val.count('+') == 1:





print(cnt)


