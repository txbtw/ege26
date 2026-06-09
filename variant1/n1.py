from itertools import *

graph = 'ab be ef fg gh ha ad dc bc eg'.split()
matrix0 = '68 568 457 35 234 12 38 127'.split()

print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix0[i.index(y)] for x,y in graph):
        print(*i)