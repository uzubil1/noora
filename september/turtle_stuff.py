"""
import turtle at the top of your program.
Add a function called "test_drive" and use it to issue commands to your turtle. Remember the turtle can:
Move forward some distance, e.g. turtle.forward(100)
Turn left or right some number of degrees, e.g. turtle.left(87)


Turn to face a specific angle, e.g. turtle.setheading(127)
Raise or lower the pen, i.e. turtle.up() & turtle.down()
Warp to a specific coordinate on the screen, e.g. turtle.goto(50, 50)
Return to the home position in the center, i.e. turtle.home()
Draw circles of a specified radius, e.g. turtle.circle(25)
"""

import turtle

def test_drive():
    turtle.speed(1)
    turtle.forward(100)
    turtle.left(87)
    
    turtle.setheading(127)
    turtle.up()
    turtle.down()
    turtle.goto(50, 50)
    turtle.circle(50)
    
    
def main():
    test_drive()
    input("Press enter to continue...")


main()
    

