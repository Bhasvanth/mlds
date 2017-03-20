from turtle import *
 
lineLen = inc = 20      # Line starts this long, grows this much
max = 800               # until it's this long
turn = 90               # try different numbers, e.g. 120
 
#   The line grows longer until it fills the window
while lineLen < max:
    #   https://docs.python.org/3/library/turtle.html#turtle.forward
    forward(lineLen)
    #   https://docs.python.org/3/library/turtle.html#turtle.right
    right (turn)
    lineLen += inc
 
#   https://docs.python.org/3/library/turtle.html#turtle.done
done()
