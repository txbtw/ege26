from math import *

def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/9032_b.txt') as file:
    stars = []
    dots = []
    for i in file:
        x, y ,data = i.replace(',','.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'L':
            stars.append(dots[-1])

cluster_1 = [d for d in dots if d[1] < 15]# big
cluster_2 = [d for d in dots if 15 < d[1] < 22]#mid
cluster_3 = [d for d in dots if   d[1] > 24]#small

cen_1 = cen(cluster_1)
cen_2 = cen(cluster_2)
cen_3 = cen(cluster_3)

stars_1 = [d for d in stars if d[1] < 15]
stars_2 = [d for d in stars if 15 < d[1] < 22]
stars_3 = [d for d in stars if d[1] > 24]

b1 = [dist(cen_3, cen_1)]
b2= []

for s1 in stars_1:
    for s2 in stars_2:
        b2.append(dist(s1, s2))

for s1 in stars_2:
    for s2 in stars_3:
        b2.append(dist(s1, s2))

for s1 in stars_1:
    for s2 in stars_3:
        b2.append(dist(s1, s2))

print(b1[0] * 10000)
print(max(b2) * 10000)


