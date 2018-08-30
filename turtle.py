from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(16):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

carl = Turtle()
carl.color('yellow')
carl.shape('turtle')

carl.penup()
carl.goto(-160, 80)
carl.pendown()

dennis = Turtle()
dennis.color('green')
dennis.shape('turtle')

dennis.penup()
dennis.goto(-160, 90)
dennis.pendown()

for turn in range(100):
        ada.forward(randint(1,5))
        bob.forward(randint(1,5))
        carl.forward(randint(1,5))
        dennis.forward(randint(1,5))
