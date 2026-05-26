import re
with open(r'./files/24_25361.txt') as file:
    data = file.readline()

#2----F--F-----F-F--F----F---F--F--F---F---F------

pattern = r'[02468]([^F02468]*F){76}[^F02468]*'

match = [m.group() for m in re.finditer(pattern, data)]
print(len(max(match, key=len)))