def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
new_num = 0
for n in range(1, 100000):
    r = convert(n, 4)
    if sum(map(int, r)) % 3 == 0:
        for i in num:
            if i == '0':
                new_num += '2'
            elif i == '2':
                new_num += '0'
            else:
                new_num += i
    else:
        r = r + '33'



