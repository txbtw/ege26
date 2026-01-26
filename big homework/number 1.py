from itertools import *

graph = 'hg gc cf fa ae eh de df db bh bg'.split()
mtrx = '367 568 18 58 247 127 156 234'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in mtrx[i.index(y)] for x, y in graph):
        print(*i)
        h