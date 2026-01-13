from turtle import *
screensize(3000, 3000)
tracer(0)
m = 15
lt(90)
for i in range(2):
    fd(14 * m)
    lt(270)
    bk(12 * m)
    rt(90)
up()
fd(9 * m)
rt(90)
bk(7 * m)
lt(90)
down()
for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()

for x in range(-15, 2):
    for y in range(-10, 15):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()

print(15*13)