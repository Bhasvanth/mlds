#!/usr/bin/python3

from turtle import *

def draw_square(tObj, width):
    for i in range(4):
        tObj.forward(width)
        tObj.left(90)
 
if __name__ == "__main__":
    tObj = Turtle()
    tObj.pen(shown="False")

    for i in range(15):
        size = i + 20
        draw_square(tObj, size)
        tObj.forward(10)
        tObj.right(18)


    done()
