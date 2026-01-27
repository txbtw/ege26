
for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        
