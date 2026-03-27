with open(r'.\files9\17522.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    line = sorted(line)
    if line[-1] < line[0] + line[1] + line[2]:
        u1 = line[0] == line[1]
        u2 = line[1] == line[2]
        u3 = line[2] == line[3]
        if (u1 + u2 + u3) == 1:
            cnt += 1
print(cnt)