with open(r'.\files9\23268.txt') as  file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        pov = [i for i in line if line.count(i) > 1]
        ne_pov = [i for i in line if line.count(i) == 1]
        if sum(pov) / len(pov) < max(ne_pov):
            print(pos)
            break
