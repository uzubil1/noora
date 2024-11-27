
# Do NOT give the program name as turtle
# because turtle is a resreved library name by python

import turtle 

def draw():
    turtle.speed(1)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    
def main():
    draw()
    input("press enter to exit")
main()

