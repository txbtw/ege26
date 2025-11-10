from turtle import *
screensize(3000, 3000)
tracer(0)
m = 15
fd(100)
lt(90)

lt(270)
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
for x in range(-5, 30):
    for y in range(-30, 10):
        goto(x * m, y * m)
        dot(3, 'red')


update()
done()

ответ: 97,5  в ответе другой. умножил сторону которую нам известно на высоту и разделил,
перепроверил все ходы, по идеи правильно, не знаю в чем ошибка

