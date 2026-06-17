from math import *

def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/29081_a.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append([float(x), float(y)])
        if data == 'VII':
            stars.append([float(x), float(y)])

cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if d[1] > 8]

stars_1 = [d for d in stars if d[1] < 8]
stars_2 = [d for d in stars if d[1] > 8]
cen_1 = cen(cluster_1)
cen_2 = cen(cluster_2)

dist_1 = [dist(cen_1, s) for s in stars_1]
dist_2 = [dist(cen_2, s) for s in stars_2]
print(max(dist_1 + dist_2) * 10000)





