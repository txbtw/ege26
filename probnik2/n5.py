def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 10000):
    r = convert(n, 4)
    if n % 4 == 0:
        r += r[:2]
    else:
        r += convert(((n % 4) * 4), 4)
    r = int(r, 4)
    if r > 291:
        ans.append(r)
print(min(ans))
