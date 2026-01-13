print('w x y z')
for w in range(2):
    for y in range(2):
        for x in range(2):
            for z in range(2):
                f = (z <= y) or ((w <= x)<=y)
                if not f:
                    print(w, y, x, z)