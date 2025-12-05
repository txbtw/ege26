def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = convert(n, 5)
    if r[-1] == '0':
        r = r.replace('1', '*')
        r = r.replace('4', '1')
        r = r.replace('*', '4')
        r = '33' + r
    else:
        r = '3' + r[1:] + '42'
    r = int(r, 5)
    if r < 1922:
        ans.append([r, n])

maxr = max(ans)[0]
minn =[]
all_n = []
for r, n in ans:
    if r == maxr:
        all_n.append(n)
print(min(all_n))



