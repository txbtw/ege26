from itertools import *
graph = 'ag gf fb bd de ea cb cd cg'.split()
matrix = '45 345 256 127 123 37 46'.split()

print(*range(1, 9))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)lo