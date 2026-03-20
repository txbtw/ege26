from string import *

for x in printable[:22]:
    num1 = int(f'56{x}c20', 22)
    num2 = int(f'89f{x}2', 22)
    num3 = int(f'h24{x}k21', 22)
    num = num1 + num2 + num3
    if num % 21 == 0:
        print(num // 21)