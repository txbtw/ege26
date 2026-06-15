with open(r'./files9/28930.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    if line == sorted(set(line)):
        if (min(line) + max(line)) <= (sum(line) - (min(line) + max(line))):
            cnt += 1
print(cnt)