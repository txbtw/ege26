import re
from string import *
with open(r'..\files\24_21421.txt') as file:
    data = file.readline().lower()




pattern = r'[1-9AB][0-9AB]*[02468A]'

match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))

###########################################

#as8bfbef0sdjsbdasb9092763ubjvs88091238ahs
aplh = digits + ascii_uppercase

for i in printable[12:]:
    data = data.replace(i, ' ')

data = data.split()

ans = 0

# for i in data:
#     i = i.lstrip('0').rstrip('13579B')
#     ans = max(ans, len(i))
anss = 0
for i in data:
    while i and  i[0] == '0':
        i = i[1:]
    while i and i[-1] in '13579B':
        i = i[:-1]
    anss= max(anss, len(i))
print(anss)