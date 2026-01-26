ans = []
for n in range(1, 100000):
    r = f'{n:b}'
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin((n%3) * 3)[2:]
    r = int(r, 2)
    if r > 151:
        ans.append(r)
print(min(ans))