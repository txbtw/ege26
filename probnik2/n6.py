from turtle import *

screensize(5000, 5000)
tracer(0)
lt(90)
m = 15
for i in range(4):
    fd(10 * m)
    rt(270)
up()
fd(3 * m)
rt(270)
fd(5* m)
rt(90)
down()
for i in range(2):
    fd(10 * m)
    rt(270)
    fd(12 * m)
    rt(270)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()