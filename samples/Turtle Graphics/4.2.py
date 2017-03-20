#!/usr/bin/python3
from turtle import *

def drawSquare(tObj, width):
    for i in range(4):
        tObj.forward(width)
        tObj.left(90)



tObj = Turtle()
bgcolor("green")
tObj.color("red")

for i in range(1,7):
    size = (40 * i)
    drawSquare(tObj, size)
    tObj.penup()
    tObj.right(90)
    tObj.forward(20)
    tObj.setx(tObj.xcor()-20)
    tObj.left(90)
    tObj.pendown()


done()
     
