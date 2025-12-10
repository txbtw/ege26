from itertools import product
cnt = 0
for val in product('котбус', repeat=8):
    val = ''.join(val)
    if val[0] not in 'оу' and 'кот' in val:
        cnt += 1

print(cnt)
