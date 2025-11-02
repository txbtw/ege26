from turtle import *

screensize(3000, 3000)
tracer(False)
m = 7


for i in range(4):
    fd(19 * m)
    rt(90 * m)
    fd(90 * m)
    rt(90 * m)

up()

fd(2 * m)
rt(90 * m)
fd(8 * m)
lt(90 * m)

down()

for i in range(4):
    fd(93 * m)
    rt(90 * m)
    fd(97 * m)
    rt(90 * m)

for x in range(-150, 190):
    for y in range(-150, 190):
        goto(x * m, y * m)
        dot(3, 'red')


update()
done()

#че то фигня какая то получилась.......