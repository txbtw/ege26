from string import printable as alph
ans = []
for x in alph[:15]:
    m = int(f'432{x}3', 15)
    n = int(f'86{x}86', 15)
    for a in range(1, 1000000):
        if (m + a) % n == 0:
            ans.append(a)
print(min(ans))