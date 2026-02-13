from itertools import *
def f(x):
    p = 10 <= x <= 150
    q = 160 <= x <= 250
    r = 240 <= x <= 300
    a = a1<= x <= a2
    return (q <= p) or ((not a) <= r)
ans = []
lineA = [10, 150, 160, 240, 250]
lineX = [11, 151, 161, 241]
for a1, a2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(a2-a1)

print(min(ans))