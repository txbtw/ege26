from itertools import *
graph = 'гд де дж же ев вб ва ба аг'.split()
matrix = '25 137 267 56 146 345 23'.split()
print(*range(1,9))
for i in permutations('абвгдеж'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)