with open(r'.\files\7030.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [2, 2, 2]:
