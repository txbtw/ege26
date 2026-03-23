from itertools import combinations


def f(x):
    p = 5 <= x <= 280
    q = 295 <= x <= 400
    r = 375 <= x <= 450
    a = a1 <= x <= a2
    return (q <= p) or ((not a) <= r)

lineA = [5,280, 295, 375, 400, 450]
lineX = [6, 290, 300, 380, 401]
ans = []
for a1, a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(a2 - a1)
print(min(ans))