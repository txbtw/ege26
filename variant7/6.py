from turtle import *

screensize(5000, 5000)
lt(90)
tracer(0)
m = 15

rt(270)
for i in range(2):
    fd(8 * m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3 * m)
    rt(240)
rt(240)
for i in range(2):
    fd(14 * m)
    rt(120)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()