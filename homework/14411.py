from itertools import product
al = sorted('сублимаця')
for pos, val in enumerate(product(al, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[-1] != 'я' and val.count('у') + val.count('и') + val.count('а') + val.count('я')== 2:
        print(pos)
