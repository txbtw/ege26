import re

with open(r'.\files\24_5171.txt') as file:
    data = file.readline()

pattern = r'(CA)*C?'
match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))
