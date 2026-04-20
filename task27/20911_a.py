from math import *

def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\20911_a.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] > 0]
cluster_2 = [dot for dot in dots if dot[1] < 0]

center_1 = cen(cluster_1)
center_2 = cen(cluster_2)

print((center_1[0] + center_2[0]) /2 * 10000)
print((center_1[1] + center_2[1]) /2 * 10000)