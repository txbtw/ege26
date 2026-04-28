from math import *

def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]



with open(r'.\files\29080_b.txt') as file:
    stars = []
    dots = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
            stars.append(dots[-1])

cluster_1 = [[dot for dot in dots if dot[1] < 16], #big
             [dot for dot in stars if dot[1] < 16]]
cluster_2 = [[dot for dot in dots if 16 <dot[1] < 23], #mid
             [dot for dot in stars if 16 <dot[1] < 23]]
cluster_3 = [[dot for dot in dots if dot[1] > 23], # small
             [dot for dot in stars if dot[1] > 23]]


stars_1 = [dot for dot in stars if dot[1] < 16]
stars_2 = [dot for dot in stars if 16 <dot[1] < 23]
stars_3 = [dot for dot in stars if dot[1] > 23]

center_1 = cen(cluster_1[0])
center_2 = cen(cluster_3[0])

print(dist(center_1, center_2) * 10000)
ans = []
for s1 in stars_1:
    for s2 in stars_2:
        ans.append(dist(s1, s2))

for s1 in stars_1:
    for s2 in stars_3:
        ans.append(dist(s1, s2))

for s1 in stars_2:
    for s2 in stars_3:
        ans.append(dist(s1, s2))
print(max(ans) * 10000)
