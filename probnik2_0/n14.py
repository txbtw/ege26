from string import *
for x in printable[:29]:
    num1 = int(f'463{x}7921', 29)
    num2 = int(f'8241{x}153', 29)
    num = num1 + num2
    if num % 28 == 0:
        print(x, num // 28)