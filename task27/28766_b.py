from math import *
from itertools import *
def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\28766_b.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float, [x, y])))


cluster_1 = [dot for dot in dots if dot[1] < 15]
cluster_2 = [dot for dot in dots if dot[1] > 15 and dot[1] < 22]
cluster_3 = [dot for dot in dots if dot[1] > 22]

s_cluster_1 = [dot for dot in stars if dot[1] < 15]
s_cluster_2 = [dot for dot in stars if dot[1] > 15 and dot[1] < 22]
s_cluster_3 = [dot for dot in stars if dot[1] > 22]
b1 = []
for s1 in s_cluster_1:
    for s2 in s_cluster_1:
        if s1 != s2:
            b1.append(dist(s1, s2))

for s1 in s_cluster_2:
    for s2 in s_cluster_2:
        if s1 != s2:
            b1.append(dist(s1, s2))

for s1 in s_cluster_3:
    for s2 in s_cluster_3:
        if s1 != s2:
            b1.append(dist(s1, s2))

print(min(b1) * 10000)

print(len(s_cluster_1)) # max
print(len(s_cluster_2)) # min

print(dist(cen(cluster_1), cen(cluster_2)) * 10000)


######################## задроченный код

with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float, [x, y])))

cluster_1 = [[d for d in dots if 23 < d[1]],
             [d for d in stars if 23 < d[1]]]
cluster_2 = [[d for d in dots if 16 < d[1] < 23],
             [d for d in stars if 16 < d[1] < 23]]
cluster_3 = [[d for d in dots if d[1] < 16],
             [d for d in stars if d[1] < 16]]
clusters = [cluster_1, cluster_2, cluster_3]

B1 = []
for cluster in clusters:
    B1 += [dist(s1, s2) for s1, s2 in combinations(cluster[1], 2)]

min_center = center(min(clusters, key=lambda x: len(x[1]))[0])
max_center = center(max(clusters, key=lambda x: len(x[1]))[0])

print(min(B1) * 10_000, dist(min_center, max_center) * 10_000)



