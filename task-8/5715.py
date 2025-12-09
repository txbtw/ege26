from itertools import product
al = 'пкб'
cnt = 0
for val in product(al, repeat=15):
    val = ''.join(val)
    if val.count('к') > val.count('п') > val.count('б'):
        cnt += 1
print(cnt)