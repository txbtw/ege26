def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(10, 1000):
    r =  convert(n, 3)
    if n % 4 == 0:r += r[-3:]
    else:r = '1' + r + '20'
    r = int(r, 3)
    if r > 423:
        ans.append(r)
print(min(ans))


