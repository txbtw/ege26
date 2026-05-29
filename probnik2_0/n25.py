def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}
    if d and len(d) > 1:
        return min(d) + max(d)
    else:
        return 0
cnt = 0
for i in range(5_400_001, 10**20):
    F = f(i)
    if F > 60000 and str(F) == str(F)[::-1]:
        print(i, F)
        cnt += 1
        if cnt == 5:
            break







