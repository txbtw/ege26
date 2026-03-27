f = [0] * 2200

for i in range(2200):
    if i <= 5: f[i] = 1
    else: f[i] = i + f[i - 2]

print(f[2126] - f[2122])