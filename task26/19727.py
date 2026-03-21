with open(r'.\files\26.2_19727.txt') as file:
    m, n = map(int, file.readline().split())
    weigh = [int(i) for i in file]

weigh = sorted(weigh)
ans = []
for bidon in weigh:
    if sum(ans) + bidon <= m:
        ans.append(bidon)
free_space = m - sum(ans[:-1])
print(len(ans), len([i for i in weigh if i > free_space]))

