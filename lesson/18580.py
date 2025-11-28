from string import printable as al
for x in al[:25]:
    num1 = int(f'a4{x}7f2', 25)
    num2 = int(f'n{x}g5{x}h', 25)
    num3 = int(f'74{x}m26', 25)
    num = num1 + num2 + num3
    if num % 24 == 0:
        print(x, num // 24)