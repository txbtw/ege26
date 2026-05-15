import re

with open(r'../files/15339.txt') as file:
    data = file.readline()

pattern = r'(([ABC][6789])*|([6789][ABC])*)*'
match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))
