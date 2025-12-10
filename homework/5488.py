from itertools import product
cnt = 0
for val in product('сгсгсг', repeat=8):
    val = ''.join(val)
    if val.count('г') > val.count('с') :
        cnt += 1
print(cnt)