from itertools import permutations
cnt = 0
for val in set(permutations('сортировка')):
    val = ''.join(val)
    for i in 'сртвк':
        val = val.replace(i, '*')
    for r in 'оиа':
        val = val.replace(r, '+')
    if '***' not in val and '+++' not in val:
        cnt += 1
print(cnt)
