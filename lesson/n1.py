from itertools import *

def f(x):
    b = 24 <= x <= 90
    c = 47 <= x <= 115
    a = a1 <= x <= a2
    return c <= (((not a) and b) <= (not c))
ans = []
lineA = [24, 47, 90, 115]
lineX = [25, 48, 100]
for a1, a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(a2 - a1)
print(min(ans))