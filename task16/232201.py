f = [0] * 7000

for n in range(7000):
    if n < 10: f[n] = n
    else: f[n] = 3 * n + f[n - 3]

print((f[6250] + 2 * f[6244]) // f[6238])