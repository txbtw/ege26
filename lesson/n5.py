ans = []
for n in range(1, 100000):
    r = f'{n:b}'
    for i in r:
        if i == '0':
            r = r.replace(i, '00')
        if i == '1':
            r = r.replace(i, '11')
    r = int(r, 2)
    if r > 63:
        ans.append(r)
print(min(ans))
