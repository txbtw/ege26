from fnmatch import *

for i in range(14036 - 14036 % 22768, 10**8 + 1, 22786):
    if fnmatch(str(i), '1N03*6*'):
        print(i, )