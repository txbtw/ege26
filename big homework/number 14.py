def convert(numx, sys):
    res = ''
    while numx:
        res += str(numx % sys)
        numx //= sys
    return res[::-1]

for x in range(1, 2006):
    num = convert(4 ** 163 * 5 + 12 ** 62 - x, 5)
    if num.count('1') < num.count('4'):
        print(x)