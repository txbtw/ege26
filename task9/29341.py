with open(r'./files9/29341.txt') as file:
    data = [list(map(int, i.split())) for i in file]


cnt = 0
for line in data:
    line = sorted(line)
    if line[-1] < sum(line) - line[-1]:
        if line[0] + line[-1] != line[1] + line[2]:
            cnt += 1
print(cnt)