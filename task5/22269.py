


def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []

for n in range(1, 100000):
    r = convert(n, 5)
    new_num = ''
    if r[-1:] == 0:
        for i in r:
            if i == '1':
                new_num += '4'
            elif i == '4':
                new_num += '1'
            else:
                new_num += i
        r = '33' + r
    else:
        r = r[:1] + '42'
    r = int(r, 5)
    if r < 1922:
        ans.append([r, n])
        print(min(ans))
