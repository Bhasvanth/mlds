#!/usr/bin/python3
from turtle import *

def drawSquare(tObj, width):
    for i in range(4):
        tObj.forward(width)
        tObj.left(90)



tObj = Turtle()
tObj.color("red")

for i in range(36):
    drawSquare(tObj, 50)
    tObj.right(10)

done()
     
