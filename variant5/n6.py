from turtle import *

screensize(4000, 4000)
tracer(0)
lt(90)
m = 25

for i in range(5):
    fd(6 * m)
    rt(90)
    fd(3* m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(2 * m)
rt(90)
down()
for i in range(8):
    fd(8 * m)
    rt(90)
    fd(5 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(2 * m)
lt(90)
down()
for i in range(4):
    fd(5 * m)
    lt(90)
up()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()