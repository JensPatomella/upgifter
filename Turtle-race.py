from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(16):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
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

for turn in range(30):
  ada.right(12)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(30):
  bob.left(12)

bing = Turtle()
bing.shape('turtle')
bing.color('green')

bing.penup()
bing.goto(-160, 40)
bing.pendown()

for turn in range(30):
  bing.right(12)

bong = Turtle()
bong.shape('turtle')
bong.color('orange')

bong.penup()
bong.goto(-160, 10)
bong.pendown()

for turn in range(30):
  bong.left(12)

for turn in range(105):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  bing.forward(randint(1,5))
  bong.forward(randint(1,5))
  
exitonclick()