import re

with open(r'../files/8835.txt') as file:
    data = file.readline()
#
# pattern = r'([^M\.]*M){112}[^M\.]*\.'
#
# match = [m.group() for m in re.finditer(pattern, data)]
#
# print(len(max(match, key=len)))


#########################################################

data = data.split('M')

ans = 0
for i in range(len(data) - 112):
    line_1 = data[i]
    line = 'M' + 'M'.join(data[i + 1:i + 112]) + 'M'
    line_113 = data[i + 112]
    if line.count('.') != 0 or line_113.count('.') == 0: continue
    if '.' in line_1:
        line_1 = line_1[line_1.rfind('.') + 1:]
    line_113 = line_113[:line_113.find('.')+1]
    line = line_1 + line + line_113
    ans = max(ans, len(line))

print(ans)

##########################################

data = data.replace('.', '.*')
data = data.split('*')[:-1]

ans = 0
for line in data:
    count_m = line.count('M')
    if count_m == 112:
        ans = max(ans, len(line))
    elif count_m > 112:
        while count_m > 112:
            if line[0] == 'M': count_m -= 1
            line = line[1:]
        ans = max(ans, len(line))
print(ans)




