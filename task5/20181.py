for n in range(1, 10000101):
    r = f'{n:b}'
    if n % 2 == 0:
        r += f'{r.count('1'):b}'
    else:
        r = '1' + r + '101'
    r = int(r, 2)
    if r > 350:
        print(n)
        break





