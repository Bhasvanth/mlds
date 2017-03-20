#!/usr/bin/python3
from turtle import * 


def triangle (a,b,c, angle1, angle2, angle3):
    turtleObj = Turtle()
    turtleObj.speed("slow")
    turtleObj.forward(a)
    turtleObj.left((180-angle1))
    turtleObj.forward(b)
    turtleObj.left((180-angle2))
    turtleObj.forward(c)
    
if __name__ == "__main__":
#    triangle(80,80,80, 60,60,60)
    triangle(40,55,40, 45,45,90) 
    done()
