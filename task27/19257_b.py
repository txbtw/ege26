from math import *

def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_b_19257.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[0] < 0]
cluster_2 = [dot for dot in dots if dot[0] > 1 and 2 <= dot[1] <= 7]
cluster_3 = [dot for dot in dots if dot[0] > 2 and 8 <= dot[1] <= 13]

center_1 = cen(cluster_1)
center_2 = cen(cluster_2)
center_3 = cen(cluster_3)

print((center_1[0] + center_2[0] + center_3[0]) / 3 * 10000)
print((center_1[1] + center_2[1] + center_3[1]) / 3 * 10000)