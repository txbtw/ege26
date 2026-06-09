from math import *
def cen(cluster):
    res  = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]


with open(r'27_b') as file:
    stars = []
    dots = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:] == 'III':
            stars.append(dots[-1])


# cluster_1 = [d for d in dots if d[1] < 8]
# cluster_2 = [d for d in dots if d[1] > 8] # small
#
# stars_1 = [dot for dot in stars if dot[1] > 8]
# stars_2 = [dot for dot in stars if dot[1] < 8]
#
#
# center_1 = cen(cluster_1)
# center_2 = cen(cluster_2)
# ans = []
# ans.append(max(dist(center_2, s) for s in stars_1))
# ans.append(max(dist(center_1, s) for s in stars_2))
#
# print(min(ans) * 10000)
# print(max(ans) * 10000)


cluster_1 = [d for d in dots if d[1] < 15]# наимешьнийц
cluster_2 = [d for d in dots if 15 < d[1] < 23] # bigges
cluster_3 = [d for d in dots if 23 < d[1] < 30] # mid

stars_1 = [d for d in stars if d[1] < 15]
stars_2 = [d for d in dots if 15 < d[1] < 23]
stars_3 = [d for d in dots if 23 < d[1] < 30]


center_1 = cen(cluster_1)
center_2 = cen(cluster_2)
center_3 = cen(cluster_3)
ans = []

ans.append(max(dist(s1, s2) for s1 in stars_1 for s2 in stars_2) * 10000)
ans.append(max(dist(s2, s3) for s2 in stars_2 for s3 in stars_3) * 10000)
ans.append(max(dist(s1, s3) for s1 in stars_1 for s3 in stars_3) * 10000)

print(max(ans))


