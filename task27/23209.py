from math import *
def cen(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\23209_a') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_a_1 = [dot for dot in dots if dot[1] < 15]
cluster_a_2 = [dot for dot in dots if dot[1] > 15]

center_a_1 = cen(cluster_a_1)
center_a_2 = cen(cluster_a_2)

print(max(center_a_1[0], center_a_2[0]) * 10000)
print(max(center_a_1[1], center_a_2[1]) * 10000)



with open(r'.\files\23209_b') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


center_b_1 = cen(cluster_b_1)
center_b_2 = cen(cluster_b_2)
center_b_3 = cen(cluster_b_3)

cluster_B_1 = [d for d in dots if 0 < d[1] < 15]
cluster_B_2 = [d for d in dots if 15 < d[1] < 21]
cluster_B_3 = [d for d in dots if 21 < d[1] < 30]
clusters_B = [cluster_B_1, cluster_B_2, cluster_B_3]

max_cluster = center(max(clusters_B, key=len))
min_cluster = center(min(clusters_B, key=len))

print((max_cluster[0] - min_cluster[0]) * 10_000)
print((max_cluster[1] - min_cluster[1]) * 10_000)


print((center_b_1[0] - center_b_3[0]) * 10000)
print((center_b_1[1] - center_b_3[1]) * 10000)

