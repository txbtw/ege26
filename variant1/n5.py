ans = []

for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '1'
    else:
        r = '11' + r[2:] + '0'
    r = int(r, 2)
    if n < 16:
        ans.append(r)
print(max(ans))