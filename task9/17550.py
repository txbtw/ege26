with open(r'.\files9\17550.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    amount = [line.count(i) for i in line]
    if sorted(amount) == [1, 1, 1, 3, 3, 3]:
        summ_2 = sum(i for i in line if line.count(i) > 1)
        summ_1 = sum(i for i in line if line.count(i) == 1)
        if summ_2 ** 2 > summ_1 ** 2:
            cnt += 1
print(cnt)
