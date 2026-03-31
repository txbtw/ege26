f = [0] * 300000
g = [0] * 300000
for n in range(0, 300000):
    if n >= 128: f[n] = f[n- 5] + 1092
    else: f[n] = 5 * g[n - 7] + 29

for n in range(300000, 0, -1):
    if n > 303728: g[n] = n - 15
    else: g[n] = (g[n + 8] / 2) - 109

print(f[2049])