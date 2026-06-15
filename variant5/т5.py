def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 1000):
    r = convert(n, 8)
    if r[0] == 5:
        r = r.replace('2', '*')
        r = r.replace('1', '2')
        r = r.replace('*', '1')
        r = '11' + r
    else:
        r = '2' + r[1:] + '10'
    r = int(r, 8)
    if r == 1352:
        ans.append(n)
print(max(ans))