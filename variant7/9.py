with open(r'./files/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]
ans = []
for pos, line in enumerate(data, start=1):
    if len(set(line)) == len(line):
        if (max(line) - min(line)) ** 3 >= (sum(line) - max(line) - min(line)) ** 2:
            ans.append(pos)
print(sum(ans))