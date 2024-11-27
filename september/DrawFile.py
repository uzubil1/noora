"""_summary_
turtle is a python library or module
that helps in drawing different shapes
just like you draw in mspaint

In the code below, we draw 3 squares, fill colors in them,
setup background color, setup pencolor, pensize, 
"""
import turtle

def square(px, ang, color):
    turtle.speed(1)
    turtle.pensize(10)    
    turtle.bgcolor('pink')
    turtle.fillcolor(color)
    turtle.pencolor('white')
    # to fill the color in the square
    turtle.begin_fill()
    turtle.forward(px)
    turtle.left(ang)
    turtle.forward(px)
    turtle.left(ang)
    turtle.forward(px)
    turtle.left(ang)
    turtle.forward(px)
    turtle.left(ang)
    turtle.end_fill()
    
def main():
    fillColor= input("Please select a color to fill the squares")
    
    pixels= 150
    angle=90
    square(pixels, angle, fillColor)
    
    fillColor= input("Please select another color to fill the squares")
    pixels= 100
    angle=90
    square(pixels, angle, fillColor)
    
    fillColor= input("Please select another color to fill the squares")
    pixels= 70
    angle=90
    square(pixels, angle,fillColor)
    
    input("Please enter any key")
    
main()




