from turtle import*
m = 20
tracer(0)
screensize(2000*2000)
pendown()
lt(90)
for i in range(5):
    fd(8*m)
    rt(90)
    fd(11*m)
    rt(90)
penup()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(5,'red')
        done