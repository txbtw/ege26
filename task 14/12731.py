from string import printable as al
for x in al[:13]:
    for x in al[:16]:
        for x in al[:15]:
            num1 = int(f'9{x}1011', 13)
            num2 = int(f'{x}4612', 16)
            num3 = int(f'117{x}', 15)
            num = num1 + num2 - num3
            if num % 14 == 0:
                print(x, num // 14)