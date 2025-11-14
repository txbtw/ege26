for N in range(1, 100000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 1:
        R = '10' + R
    else:
        R = '1' + R + '10'
    R = int(R, 2)
    if R < 30:
        print(N)

