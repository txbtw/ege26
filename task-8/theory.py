from itertools import *
alph = '123131l2rsdfpl'
# product - функция которая формирует все возможные
# комбинации символов с повторением  длины repeat
for val in product(alph, repeat=2):
    val = ''.join(val)
    print(val)

# permutations функция которая формирует все возможные
# перестановки символов
for val in permutations(alph):
    val = ''.join(val)
#enumirate - нумирует элементы начиная со старт
res = enumerate(alph, start=1)
print(*res)


