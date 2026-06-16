from itertools import *

def f(x):
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    a = a1 <=x <= a2
    return p <= ((q and (not a)) <= (not p))

lineA =[25,40, 64, 115]
lineX = [26, 41, 65]
ans = []
for a1, a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(a2 - a1)
print(min(ans))