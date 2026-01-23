from itertools import combinations


def f(x):
    b = 54 <= x <= 120
    c = 78 <= x <= 151
    a = a1 <= x <= a2
    return c <= ((b and (not a)) <= (not c))

ans = []
lineA = [54, 78, 120, 151]
lineX = [55, 79, 121]
for a1,a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(a2-a1)
print(min(ans))