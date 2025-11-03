from turtle import *

screensize(3000, 3000)

tracer(False)

m = 15

for i in range(9):
    fd(22 * m )
    rt(90)
    fd(6 * m)
    rt(90)
up()

fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()

for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)
down()

update()
done()

up()

for x in range(0, 130):
    for y in range(0, 130):
        goto(x * m, y * m)
        dot(5, 'black')

# у меня почему-то точки не расставляются, хотя dot же есть

