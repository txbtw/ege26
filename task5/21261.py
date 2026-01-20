def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
new_num = 0
ans = []
for n in range(1, 100000):
    r = convert(n, 4)
    if sum(map(int, r)) % 3 == 0:
       r = r.replace('0', '*')
       r = r.replace('2', '0')
       r = r.replace('*', '2')
       r = '32' + r
    else:
        r = r[0] + '10' + r[3:] + '33'
    r = int(r, 4)
    if r == 335:
        ans.append(n)
#     if r > 320:
# #         ansr.append(r)
# #         ansn.append(n)
# # minr = min(ansr)
# # ansmaxn = []
# # for i in range(len(ansr)):
# #     if ansr[i] == minr:
# #         ansmaxn.append(ansn[i])
# # print(max(ansmaxn))


print(max(ans))













