from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 3001):
    num = convert(9 * 11 ** 210 + 8 * 11 ** 150 - x, 11)
    if num.count('0') == 60:
        print(x)
#asn = 2992
