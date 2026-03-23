from string import *

for x in printable[:18]:
    for y in printable[9:18]:
        num1 = int(f'5{x}{y}a', 18)
        num2 = int(f'18{x}7', y)
        num = num1 + num2


