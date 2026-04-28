from math import *

def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\29079_a.txt') as file:
    stars = []
    dots = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'N' and data[2:] == 'IV':
            stars.append(dots[-1])

cluster_1 = [dot for dot in dots if dot[1] > 8]
cluster_2 = [dot for dot in dots if dot[1] < 8]

stars_1 = [dot for dot in stars if dot[1] > 8]
stars_2 = [dot for dot in stars if dot[1] < 8]


center_1 = cen(cluster_1)
center_2 = cen(cluster_2)
ans = []
ans.append((max(dist(center_1, s) for s in stars_2)))
ans.append((max(dist(center_2, s) for s in stars_1)))

print(min(ans) * 10000)
print(max(ans) * 10000)




