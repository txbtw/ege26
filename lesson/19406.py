from string import printable as al
for x in al[:35]:
    num1 = int(f'6{x}qr{x}', 35)
    num2 = int(f'{x}59sh', 35)
    num3 = int(f'ph{x}69yw', 35)
    num = num1 + num2+ num3
    if num %