def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'
ans = []
for n in range(1, 10000):
    r = convert(n, 5)
    if sum(map(int, r)) % 5 == 0:
        r = r.replace('1', '+')
        r = r.replace('0', '1')
        r = r.replace('+', '0')
        r += '14'
    else:
        r = '44' + r[2:] + '33'
    r = int(r, 5)
    if r > 370:
        ans += [[r, n]]
print(min(ans))
