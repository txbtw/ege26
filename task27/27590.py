from math import *

def anticen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]

with open(r'.\files\27590_a.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] < 8]
cluster_2 = [dot for dot in dots if dot[1] > 8]

center_1 = anticen(cluster_1)
center_2 = anticen(cluster_2)

print((center_2[0] + center_2[1]) * 10000)
print((center_1[0] + center_1[1]) * 10000)




with open(r'.\files\27590_b.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


cluster_1 = [dot for dot in dots if 10 < dot[1] < 20]
cluster_2 = [dot for dot in dots if 12 < dot[0] < 18 and 20 < dot[1] < 30]
cluster_3 = [dot for dot in dots if 18 < dot[0] < 24 and 20 < dot[1] < 30]

cen_1 = [anticen(cluster_1)]
cen_2 = [anticen(cluster_2)]
cen_3 = [anticen(cluster_3)]
print(max(cen_1))
print(max(cen_2))
print(max(cen_3))


