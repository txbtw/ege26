from itertools import product
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
for val in product('конец', repeat=5):
    cnt_1 += 1
for val in product('дракон', repeat=5):
    cnt_2 += 1
for val in product('кон', repeat=5):
    cnt_3 += 1
cnt = cnt_1 + cnt_2 - cnt_3 - cnt_3
print(cnt)
