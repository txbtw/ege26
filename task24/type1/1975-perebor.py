with open(r'../files/1975.txt') as file:
    data = file.readline()

cnt = 1
ans = 0

for i in range(len(data) - 1):
    if data[i] + data[i + 1] != 'PP':
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 1
ans = max(cnt, ans)
print(ans)

