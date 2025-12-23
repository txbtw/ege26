from itertools import *
graph = 'ce eg gf fb ba fa ac cd dh he'.split()
mtrx = '68 47 45 237 368 15 248 157'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in mtrx[i.index(y)] for x, y in graph):
        print(*i)
