from itertools import *

def f(x):
    d = 7 <= x <= 68
    c = 29 <= x <= 100
    a = a1 <= x <= a2
    return d <= (((not c) and (not a)) <= (not d))
ans = []
lineA = [7, 29, 68, 100]
lineX = [8, 30, 69]
for a1, a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(a2 - a1)
print(min(ans))