from math import *

def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]



with open(r'.\files\29080_a.txt') as file:
    stars = []
    dots = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[1] == '3':
            stars.append(dots[-1])


cluster_1 = [dot for dot in dots if dot[1] > 8] # меньш
cluster_2 = [dot for dot in dots if dot[1] < 8] # больш

center_1 = cen(cluster_1)
center_2 = cen(cluster_2)

print((max(dist(center_1, s) for s in stars)) * 10000)
print((max(dist(center_2, s) for s in stars)) * 10000)