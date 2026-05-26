import re
with open(r'../files/24_18186.txt') as file:
    data = file.readline()
ssg = r'[^AE]{2}[AE]'

pattern = rf'(?<={ssg}).*?(?={ssg})'

match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)) + 6)