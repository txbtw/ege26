cnt = 0
for x in range(1, 5556):
    num = 5**150 + 5**135 - x
    while num % 5 == 4:
        cnt += 1
        num //= 4
    if cnt == 134:
        print(x)
