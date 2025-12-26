from itertools import *
def f(x, y, z):
    return not(x == (y <= z) )

table = [
    (0, 0, 1),
    (0, 1, 1)
]
if len(set(table)) == len(table):
    for p in permutations('xyz'):
        if [f(**dict(zip(p, t))) for t in table] == [1, 0]:
            print(*p)