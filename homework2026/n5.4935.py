ans = []
for n in range(1 ,100000):
    r = f'{n:b}'
    if sum(map(int, r)) % 2 == 0:
        r = '10' + r[:-2] + '00'
    else:
        r = '11' + r[:-2] + '11'
    r = int(r, 2)
    if n < 30:
        ans.append(r)
print(max(ans))