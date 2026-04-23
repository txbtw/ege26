from math import *
def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
#
# with open(r'.\files\18677.txt') as file:
#     dots = [list(map(float, i.replace(',', '.').split())) for i in file]


#
# center = [cen(cluster) for cluster in clusters]
# print((center[0][0] + center[1][0])/ 2 * 100000)
# print((center[0][1] + center[1][1])/ 2 * 100000)


with open(r'.\files\18677_b.txt') as file:
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
    if len(cluster) > 5:
        clusters.append(cluster)
center = [cen(cluster) for cluster in clusters]

print((center[0][0] + center[1][0] + center[2][0])/ 3 * 100000)
print((center[0][1] + center[1][1] + center[2][1])/ 3 * 100000)