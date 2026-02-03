
for x in range(1, 1000):
    num7 = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    i = []
    while num7:
        i.append(num7 % 7)
        num7 //= 7
    if i.count(6) == 49:
        print(x)
        break


