import re

with open(r'./files/24_23762.txt') as file:
    data = file.readline()

data = data.split('Y')
ans = 0

for j in range(len(data) - 80):
    line_1 = 'Y'.join(data[j:j + 81])
    if line_1.count('2025') >= 90:
        ans = max(ans, len(line_1))
    else:
        continue
print(ans)
