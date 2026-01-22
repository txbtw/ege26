from itertools import *
def f(x):
    m = 32 <= x <= 68
    n = 54 <= x <= 76
    a = a1 <= x <= a2
    return not(m or n) == (not a)
lineA = [32, 54, 76, 68]
lineX = [33, 55, 77]
ans = []
for a1, a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(a2 - a1)
print(min(ans))
