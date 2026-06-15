import re

with open(r'./files/24_23206.txt') as file:
    data = file.readline()

pattern = r'[02468][^02468S]*(S[^02468S]*){35}'

match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))


############################################################

from string import  printable

with open(r'../Task24/Files/24_23206.txt') as file:
    data = file.readline()

for i in range(0, 10, 2):
    a = str(i)
    b = ' ' + a
    data = data.replace(a, b)

data = data.split()
maxi = 0

for i in data:
    cnt_S = i.count('S')
    if cnt_S == 35:
        maxi = max(maxi, len(i))
    elif cnt_S > 35:
        while cnt_S > 35:
            if i[-1] == 'S': cnt_S -= 1
            i = i[:-1]
        maxi = max(maxi, len(i))

print(maxi)