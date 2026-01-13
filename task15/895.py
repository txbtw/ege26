
from itertools import combinations
def f(x):
    c = 48 <= x <= 94
    j = 83 <= x <= 100
    a = a1 <= x <= a2
    return (not(c or j)) <= (not a)

line = []
line_a = [48, 83, 94, 100]
line_x = [60, 91, 97]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2-a1)

print(max(ans))