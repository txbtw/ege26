def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 1000):
    r = convert(n, 3)
    if n % 3 == 0: r += r[-2:]
    else: r += convert((n % 3) * 5, 3)
    r = int(r, 3)
    if r > 150:
        ans.append(r)
print(min(ans))