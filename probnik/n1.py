from itertools import *
graph ='ag gf fe ed da ab bg bc cd'.split()
mtrx = '26 147 456 236 37 134 25'.split()
print(*range(1,8))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+ 1) in mtrx[i.index(y)] for x, y in graph):
        print(*i)