from itertools import product
cnt = 0
for val in product('01234567', repeat=6):
    val = ''.join(val)
    if val[0] != '0' and '3' not in val and len(set(val)) == len(val):
        val = val.replace('0', '*')
        val = val.replace('2', '*')
        val = val.replace('4', '*')
        val = val.replace('6', '*')
        if '**' in val:
            cnt += 1
print(cnt)