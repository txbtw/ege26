with open(r'./files/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 2, 2, 2]:
        ne_pov = [i for i in line if line.count(i) == 1]
        pov = [i for i in line if line.count(i) > 1]
        pov = sorted(pov)
        if (pov[0] + pov[-1]) / 2 < ne_pov[0]:
            cnt += 1
print(cnt)