import re
with open(r'../files/12254.txt') as file:
    data = file.readline()
#
# pattern = r'(SQ|Q)?(RSQ)+(RS|R)?'
#
# match = [m.group() for m in re.finditer(pattern, data)]
#
# print(len(max(match, key=len)))



######################################################## zamena
#RSQSRQS ********** RSQRQRQSR
data = data.replace('RSQ', '***')
data = data.replace('SQ*', ' ***')
data = data.replace('Q*', ' **')
data = data.replace('*RS', '*** ')
data = data.replace('*R', '** ')

for i in 'RSQ':
    data = data.replace(i, ' ')


data = data.split()
print(len(max(data, key=len)))
