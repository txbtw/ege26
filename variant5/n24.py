import re

with open(r'./files/24_23206.txt') as file:
    data = file.readline()

pattern = r'[02468]+([13579A-Z]){35}'

match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))