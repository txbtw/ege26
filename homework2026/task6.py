from turtle import *
lt(90)
screensize(3000, 3000)
tracer(0)
m = 20

fd(30 * m)
lt(60)
fd(24 * m)
rt(240)

fd(54 * m)
lt(120)
fd(24 * m)
lt(60)
up()
fd(30 * m)
rt(90)
fd(20 * m)
lt(90)

down()
for i in range(17):
    fd(6 * m)
    lt(90)
    fd(80 * m)
    lt(90)
up()
for x in range(-21, 1):
    for y in range(30, 37):
        goto(x * m, y * m)
        dot(3, 'red')


done()
update()
#я хз как посчитать периметр, по пифагора там не считается гипотензуа