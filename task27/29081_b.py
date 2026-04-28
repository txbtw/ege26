from math import *
from itertools import *

with open(r'.\files\29081_b.txt') as file:
    stars = []
    dots = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if int(data[1]) >= 8 and data[1] in '89' and data[1] >= '8':
            stars.append(list(map(float, [x, y])))


stars_1 = [dot for dot in stars if dot[1] < 16]
stars_2 = [dot for dot in stars if 16 <dot[1] < 23]
stars_3 = [dot for dot in stars if dot[1] > 23]
ans = []
for s in stars_1:
    for i in stars_2:
        ans.append(dist(s, i))
for s in stars_1:
    for x in stars_3:
        ans.append(dist(s, x))
for s in stars_2:
    for x in stars_3:
        ans.append(dist(s, x))
print(min(ans) * 10000)
ans_1 = []
for s1 in stars_1:
    for s2 in stars_1:
        if s1 != s2:
            ans_1.append(dist(s1, s2))

for s1 in stars_2:
    for s2 in stars_2:
        if s1 != s2:
            ans_1.append(dist(s1, s2))

for s1 in stars_3:
    for s2 in stars_3:
        if s1 != s2:
            ans_1.append(dist(s1, s2))
print(sum(ans_1) / len(ans_1) * 10000)


#############################################

stars_1 = [d for d in stars if 23 < d[1]]
stars_2 = [d for d in stars if 16 < d[1] < 23]
stars_3 = [d for d in stars if d[1] < 16]
all_stars = [stars_1, stars_2, stars_3]

B1 = [dist(s1, s2) for cl1, cl2 in combinations(all_stars, 2) for s1 in cl1 for s2 in cl2]
B2 = [dist(s1, s2) for cl in all_stars for s1, s2 in combinations(cl, 2)]

print(min(B1) * 10_000, sum(B2) / len(B2) * 10_000)

############################################

B1, B2 = [], []
for s1, s2 in combinations(stars, 2):
    u = any(s1 in cl and s2 in cl for cl in all_stars)
    d = dist(s1, s2)
    if u: B2.append(d)
    else: B1.append(d)

print(min(B1) * 10_000, sum(B2) / len(B2) * 10_000)




