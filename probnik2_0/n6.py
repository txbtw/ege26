from turtle import *

screensize(5000, 5000)

m = 15
tracer(0)
lt(90)
for i in range(2):
    fd(20 * m)
    lt(270)
    fd(12 * m)
    rt(90)
up()
fd(9 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()