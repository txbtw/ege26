#системы счисления

N = 25
#bin() - переводит десятичное число в двоичную систему.
#принимает на вход int, возвращает str
# [2:] - срез, убирающий первые два символа '0b'
print(bin(N)[2:])
print(f'{N:b}')

# f'' - форматируемая строка, которая позволяет вставлять в себя переменную
# восьмеричная система счисления
print(oct(N)[2:])
print(f'{N:o}')

# шестнадцатеричная система счисления
print(hex(N)[2:])
print(f'{N:x}')

#перевод в любую систему (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
print(convert(25, 3))
print(convert(37, 7))

#перевод в любую систему (2 <= sys <= 36)
from string import printable

def convert2(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
print(convert2(24, 5))

# перевод в десятичную систему
num_bin = '101'
num_tri = '121'
num_hex = 'fa8'
print(int(num_bin, 2))

print(int(num_tri, 3))

print(int(num_hex, 16))
