from itertools import permutations
graph = 'аб бв вд де ек ег ге гв ве ва гк'.split()
matrx = '24 146 56 1267 36 23457 46'.split()
print(*range(1, 8))
for i in permutations('абвгдек'):
    if all(str(i.index(x) + 1) in matrx[i.index(y)] for x, y in graph):
        print(*i)