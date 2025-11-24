def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(10, 100000):
    r = convert(n, 3)
    if r.count('2') > r.count('1'):
        r = '22' + r
    else:
        r = '11' + r
    r = int(r, 3)
    ans.append(r)
    print(min(ans))
    break