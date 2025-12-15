from itertools import permutations
cnt = 0
for val in set(permutations('парижанка')):
    val = ''.join(val)
    for i in 'аи':
        val = val.replace(i, '*')
    if val.count('**') == 1 and '***' not in val:
        cnt += 1
print(cnt)