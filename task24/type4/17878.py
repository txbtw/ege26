import re

with open(r'../files/24_17878.txt') as file:
    data = file.readline()
num = r'([6798][06789]*|0)'
pattern = rf'({num}[-*])+{num}'

match = [m.group() for m in re.finditer(pattern, data)]


print(len(max(match, key=len)))