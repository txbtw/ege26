import re

with open(r'./files/24.txt') as file:
    data = file.readline()

pattern = r'([AE][BCD])*'

match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))
