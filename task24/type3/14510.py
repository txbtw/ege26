import re

with open(r'..\files\24_14510.txt') as file:
    data = file.readline()

for i in 'BCDFGHJKLMNPQRSTVWXZ':
    data = data.replace(i, '*')

for i in 'AEIOUY':
    data = data.replace(i, '+')

pattern = r'[**+]*'
