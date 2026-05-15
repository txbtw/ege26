import re

with open(r'../files/10105.txt') as file:
    data = file.readline()

pattern = r'([T{100,100}UVWXYZ]*)'

match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))