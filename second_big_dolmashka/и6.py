from turtle import *
screensize(5000, 5000)
tracer(0)
lt(90)

m = 20
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(20 * m)
    rt(90)
up()
bk(4 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for i in range(4):
    fd(8 * m)
    lt(90)
    fd(12 * m)
    lt(90)
up()
fd(10 * m)
down()
for i in range(4):
    fd(12 * m)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x  * m,y * m)
        dot(3, 'red')

update()
done()