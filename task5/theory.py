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
    while num:
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

#срезы
data = '123456789'
#извелечение первых двух символов
print(data[:2])
# извлечение без первых двух символов
print(data[2:])
#извлечение последних двух символов
print(data[-2:])
#извлечение без последних двух символов
print(data[:-2])

#сумма цифр числа
#двоичная система
num_1 = '101'
sum_1 = num_1.count('1')

#любая система до десятой включительно
num_2 = '122'
sum_2 = num_2.count('1') + num_2.count('2') * 2
sum_2 = sum(map(int, num_2))
print(sum_2)

#любая система до 36й включительно
num_3 = 'A'
sum_3 = sum(map(lambda x: int(x, 36), num_3))

def transform(let):
    return let(int, 36)
sum(map(transform, num_3))

#нахождение овтета через список
ans = []
ans.append(r)
print(min(ans)



# замена цифр

num = '12398'
new_num = ''
for i in num:
    if i == '1'



