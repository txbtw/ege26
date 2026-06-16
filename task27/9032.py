from math import *




def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/9032.txt') as file:
    stars = []
    dots = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'L' and data[1] == '3':
            stars.append(dots[-1])

cluster_1 = [d for d in dots if d[1] < 8]# big
cluster_2 = [d for d in dots if d[1] > 8]

cen_1 = cen(cluster_1)
cen_2 = cen(cluster_2)

a1 = [dist(cen_1, s) for s in stars]
a2 = [dist(cen_2, s) for s in stars]
print(max(a2) * 10000)
print(max(a1) * 10000)



