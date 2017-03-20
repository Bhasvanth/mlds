#!/usr/bin/python3
from turtle import *

def drawSquare(tObj, width):
    for i in range(4):
        tObj.forward(width)
        tObj.left(90)



tObj = Turtle()
bgcolor("green")
tObj.color("red")

for i in range(6):
    drawSquare(tObj, 30)
    tObj.penup()
    tObj.forward(40)
    tObj.pendown()


done()
     
