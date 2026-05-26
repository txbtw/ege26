with open(r'../files/7438.txt') as file:
    data = file.readline()

data = data.replace('DS', 'D S')
data = data.replace('SD', 'S D')
data = data.split()

ans = 0
for i in range(len(data) - 100):
    line = ''.join(data[i:i + 101])
    if line not in '0123456789':
        ans = max(ans, len(line))

print(ans)