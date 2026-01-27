from itertools import combinations


def f(x):
    p = 66 <= x <= 67
    o = 32 <= x <= 125
    t = 30 <= x <= 491
    a = a1 <= x <= a2
    return a <= (p or o or t)
lineA = [30, 32, 66, 67, 125, 491]
lineX = [31, 33, 66.5, 68, 130]

ans = []
for a1,a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(a2-a1)
print(min(ans))
#ответ неправильный