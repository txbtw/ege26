from itertools import *
graph = 'hg gc cf fa ae eh hb bg bd df de'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)