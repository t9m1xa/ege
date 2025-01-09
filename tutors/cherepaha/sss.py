from turtle import*
k = 20
tracer(0)
screensize(2000*2000)
pendown()
lt(90)
fd(15*k)
rt(90)
fd(3*k)
rt(45)
fd((5*2**0.5-5)*k)
for i in range (3):
    fd(5*k)
    rt(45)
lt(45)
fd((5*2**0.5-5)*k)
lt(135)
bk(3*k)
penup()
fd(8*k)
pendown()
for i in range(8):
    fd(6*k)
    lt(45)
penup()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(4,'red')
        done


