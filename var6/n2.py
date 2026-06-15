from itertools import *

def f(x, w, y, z):
    return (not(x == (w and (not z)))) and (y == (x and (not w)))

for i in product((0, 1), repeat=6):
    table = [
        (i[0], i[1], 0, i[2]),
        (i[3],0 , i[4], 0),
        (0, i[5], 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xwyz'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p)