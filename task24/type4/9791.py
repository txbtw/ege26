import re

with open(r'../files/24_9791.txt') as file:
    data = file.readline()

pattern = r'[1-9A-F][0-9A-F]*'

match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))