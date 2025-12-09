from itertools import *
cnt = 0
for val in product('полина', repeat=8):
    if val.count('плн') > val.count('оиа'):
        cnt += 1
print(cnt)
не допер

