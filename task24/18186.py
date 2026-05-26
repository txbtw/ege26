import re

with open(r'./files/24_18186.txt') as file:
    data = file.readline()
data = 'AAABCEAAAAABBCEECBBCBEBBEAAAHCCBCBECE'
pattern = r'([BCDFGH]{2}[AE]){1}([BCDFGH]{2}[AE]){1}'

match = [m.group() for m in re.finditer(pattern, data)]
print(match)