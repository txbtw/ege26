def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = convert(n, 9)
    if r[0] == 7:
        r = r.replace('6', '*')
        r = r.replace('3', '6')
        r = r.replace('*', '6')
    else:
        r = '3' + r[1:] + '45'
    r = int(r, 9)
    if r == 2795:
        print(n)


