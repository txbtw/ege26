import re
with open(r'../files/12254.txt') as file:
    data = file.readline()

pattern = r'((RS)*|(R)*|(SQ)*|(S)*|(Q)*)(RSQ)+((RS)*|(R)*|(SQ)*|(S)*|(Q)*)'

match = [m.group() for m in re.finditer(pattern, data)]

print(len(max(match, key=len)))