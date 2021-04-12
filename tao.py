
import turtle
import random
tao = turtle.Turtle()
tao.shape('turtle')

color = ['red','blue','green','purple','orange','pink']
tao.speed(2)
for i in range(36):
    i = random.choice(color)
    tao.color(i)
    tao.forward(100)
    tao.backward(100)
    tao.left(10)
    
for nou in range(1,30):
    i = random.choice(color)
    tao.color(i)
    tao.circle(50)
    tao.left(35)
    print('ຮອບທີ່:',nou)




'''
c = random.choice(color)
tao.home()
for i in range(1,11):
    c = random.choice(color)
    w = random.randint(10,100)
    l = random.randint(10,100)
    origin_x = random.randint(-300,300)
    origin_y = random.randint(-300,300)
    tao.goto(origin_x,origin_y)
    tao.pensize(3)
    print("-------")
    tao.color(c)
    tao.pendown()
    tao.fd(w)
    tao.rt(90)
    tao.fd(1)
    tao.rt(90)
    tao.fd(w)
    tao.rt(90)
    tao.fd(1)
    tao.penup()
    
tao.home()
'''
