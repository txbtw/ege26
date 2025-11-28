for n in range(1, 100000):
    r = f'{n:b}'
    if sum(map(int, r)) % 2 == 0:
        r = '11' + r[2:] + '1'
    else:
        if r.count('0') < r.count('1'):
            r += '0'
        else:
            r += '1'
    r = int(r, 2)
    if r > 271:
        print(n)
        break


