import re

# with open(r'../files/24_17878.txt') as file:
#     data = file.readline()
data = '-06789**09876789'
pattern = r'[^-0][06789]*[*]?[6789]+'



match = [m.group() for m in re.finditer(pattern, data)]
print(match)