from turtle import *
screensize(3000, 3000)
tracer(0)
lt(90)
m = 15
for i in range(13):
    fd(13*m)
    rt(90)
    fd(5*m)
up()
rt(90)
fd(7*m)
lt(90)
fd(10*m)
down()
for i in range(23):
    fd(8*m)
    lt(90)
    fd(11*m)
    lt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y* m)
        dot(3,'red')
update()
done()