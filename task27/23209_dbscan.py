from math import *
def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\23209_a') as file:
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

#print([len(cluster) for cluster in clusters])
centers = [cen(cluster) for cluster in clusters]


print(max(c[0] for c in centers) * 10_000)
print(max(c[1] for c in centers) * 10_000)


print(max(centers[0][0], centers[1][0]) * 10_000)
print(max(centers[0][1], centers[1][1]) * 10_000)



with open(r'.\files\23209_b') as file:
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
    if len(cluster) > 1:
        clusters.append(cluster)

# print([len(cluster) for cluster in clusters])
max_center = cen(max(clusters, key=len))
min_center = cen(min(clusters, key=len))
print((max_center[0] - min_center[0]) * 10000)
print((max_center[1] - min_center[1]) * 10000)


