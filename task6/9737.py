from turtle import *

screensize(3000, 3000)
tracer(False)
m = 18

for i in  range(2):
    fd(10 * 15)
    right(90)
    fd(18 * 15)
    rt(90)
up()

fd(5 * 15)
rt(90)
fd(7 * 15)
lt(90)

down()

for i in range(2):
    fd(10 * 15)
    rt(90)
    fd(7 * 15)
    rt(90)

up()
for x in range(-5, 20):
    for y in range(-20, 5):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
