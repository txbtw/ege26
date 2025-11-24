def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for n in range(1, 100000):
    r = convert(n, 3)
    sum_1 = sum(map(int, r))
    if sum_1 % 2 == 0:
        r = '12' + r[2:] + '0'
    else:
        r = '10' + r[2:] + '2'
    r = int(r, 3)
    if r > 105:
        print(n)
        break
#ans = 28


