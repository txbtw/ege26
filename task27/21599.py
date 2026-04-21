from math import *

def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open(r'.\files\21599_a.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] < -6]
cluster_2 = [dot for dot in dots if  -6 <dot[1] < 10/12 * dot[0] - 10]
cluster_3 = [dot for dot in dots if dot[1] > 10/12 * dot[0] - 10]

center_1 = cen(cluster_1)
center_2 = cen(cluster_2)
center_3 = cen(cluster_3)

print((center_1[0] + center_2[0] + center_3[0]) / 3 * 10000)
print((center_1[1] + center_2[1] + center_3[1]) / 3 * 10000)

with open(r'.\files\21599_b.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1b = [dot for dot in dots if dot[1] < -5]
cluster_2b = [dot for dot in dots if -5 < dot[1] < dot[1] < -10]
cluster_3b = [dot for dot in dots if dot[1] < 14/7 * dot[0] + 14 and dot[1] > -10]
cluster_4b = [dot for dot in dots if dot[0] > -10 and dot[1] > 14/7 * dot[0] + 14]
cluster_5b = [dot for dot in dots if dot[0] < -10 and dot[1] > -2 * dot[0] - 26]
cluster_6b = [dot for dot in dots if dot[1] < -2 * dot[0] - 26]