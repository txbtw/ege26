from string import printable as alps
for x in alps[:29]:
    num1 = int(f'923{x}874', 29)
    num2 = int(f'524{x}6152', 29)
    num = num1 + num2
    if num % 28 == 0:
        print(x, num // 28)
# ans = 3319197720
