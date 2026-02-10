from fnmatch import *
def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d




for i in range(202 - 202 % 53, 10**7, 53):
    if fnmatch(str(i), '*2?2*') and len(f(i)) > 30 and str(i) == str(i)[::-1]:
        print(i, sum(f(i)))