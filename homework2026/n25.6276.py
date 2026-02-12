from fnmatch import *

for n in range(10101011 - 10101011 % 2023, 10**10, 2023):
    if fnmatch(str(n), '1?1?1?1*1') and sum(map(int, str(n))) == 22:
        print(n)