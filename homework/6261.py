from itertools import product
from string import printable
cnt = 0
for val in product(printable[:8], repeat=10):
    if val.count('7') == 5 and
