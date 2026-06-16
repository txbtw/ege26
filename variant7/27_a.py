from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_a.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]


cluster_1 = [dot for dot in dots if dot[1] < 15]
cluster_2 = [dot for dot in dots if dot[1] > 15]

cen_1 = center(cluster_1)
cen_2 = center(cluster_2)

