from math import *
def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


# with open(r'.\files\18678_a.txt') as file:
#     dots = [list(map(float, i.replace(',', '.').split())) for i in file]
#
# cluster_1 = [dot for dot in dots if 0 < dot[1] < 2.5]
# cluster_2 = [dot for dot in dots if 2.5 < dot[1] < 6 and 1 < dot[0] < 6]
#
# center_1 = cen(cluster_1)
# center_2 = cen(cluster_2)
#
# print((center_1[0] + center_2[0]) / 2 * 10000)
# print((center_1[1] + center_2[1]) / 2 * 10000)



with open(r'.\files\18678_b.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)
