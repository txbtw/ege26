from string import *

print(int(max('absbwdbd'), 36) + 1)
for p in range(25, 37):
    num1 = int(f'bo', p)
    num2 = int(f'om', p)
    num3 = int(f'bl4', p)
    num4 = int(f'cng', p)
    if num1 + num2 + num3 == num4:
        print(p)






