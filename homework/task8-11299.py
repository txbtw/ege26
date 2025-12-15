from itertools import product
for pos, val in enumerate(product(sorted('бмюрн'), repeat=6), start=1):
    if pos % 2 != 0 and val[0] != 'м' and val.count('р') >= 2 and 'ю' not in val:
        print(pos)