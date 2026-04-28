from math import *
def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\29081_a.txt') as file:
    stars = []
    dots = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            stars.append(list(map(float, [x, y])))

cluster_1 = [dot for dot in dots if dot[1] > 8]
cluster_2 = [dot for dot in dots if dot[1] < 8]

center_1 = cen(cluster_1)
center_2 = cen(cluster_2)

stars_1 = [d for d in stars if d[1] > 8]
stars_2 = [d for d in stars if d[1] < 8]

print(min(dist(center_1, s) for s in stars_1) * 10000)
print(max(dist(center_2, s) for s in stars_2) * 10000)


#########################################################


####################################################

cluster_1 = [[d for d in dots if d[1] > 8],
             [d for d in stars if d[1] > 8]]
cluster_2 = [[d for d in dots if d[1] < 8],
             [d for d in stars if d[1] < 8]]
clusters = [cluster_1, cluster_2]

A1 = min(dist(cen(cl[0]), s) for cl in clusters for s in cl[1])
A2 = max(dist(cen(cl[0]), s) for cl in clusters for s in cl[1])
print(A1 * 10000, A2 * 10000)



