#!/usr/bin/python3

from turtle import *
color("blue")
shape("turtle")
stamp()
shape("arrow")
for i in range(12):
    penup()
    forward(100)
    pendown()
    forward(20)
    penup()
    forward(20)
    pendown()
    shape("turtle")
    stamp()
    shape("arrow")
    penup()
    setpos(0,0)
    right(30)

done()
