
import turtle

# Create a turtle screen
screen = turtle.Screen()

# Set the background color
screen.bgcolor("light yellow")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)

table_size = int(input("Please enter the length of one side of a table (between 10-100): "))
table_color = input("Please enter the color of the table: ")
cake_size = int(input(f"Please enter the size of the cake (between 10-{table_size}): "))
loading = input("Your cake is loading... Happy Birthday!")
# Youssef
# Function to draw a rectangle for table, table legs, and cake layers
def draw_rectangle(color, width, height):
    pen.color(color)
    pen.begin_fill()
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.end_fill()

 #Set up turtle for table
pen.penup()
pen.goto(-200, -100)
pen.pendown()

# Draw table top
draw_rectangle(table_color, 400, 50)

# Function to draw the legs of the table
def draw_leg(color, width, height):
    pen.color(color)
    pen.begin_fill()
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.end_fill()


# Draw legs of the table
pen.penup()
pen.goto(-200, -150)
pen.pendown()
draw_leg(table_color, 20, 150)

pen.penup()
pen.goto(-150, -150)
pen.pendown()
draw_leg(table_color, 20, 100)

pen.penup()
pen.goto(180, -150)
pen.pendown()
draw_leg(table_color, 20, 150)

pen.penup()
pen.goto(130, -150)
pen.pendown()
draw_leg(table_color, 20, 100)
# Saifa
# Set up turtle for cake
pen.penup()
pen.goto(-100, -70)
pen.pendown()

# Draw cake layers
draw_rectangle("pink", 200, 30)
pen.penup()
pen.goto(-100, -40)
draw_rectangle("pink", 200, 30)

pen.penup()
pen.goto(-100, -50)
draw_rectangle("light blue", 200, 5)
pen.penup()
pen.goto(-100, -67)
draw_rectangle("light blue", 200, 5)
pen.penup()
pen.goto(-100, -83)
draw_rectangle("light blue", 200, 5)

# Draw the second cake layer
pen.penup()
pen.goto(-70, -10)
draw_rectangle("light blue", 140, 30)
pen.penup()
pen.goto(-70, 20)
draw_rectangle("light blue", 140, 30)

pen.penup()
pen.goto(-70, -20)
draw_rectangle("pink", 140, 5)
pen.penup()
pen.goto(-70, -5)
draw_rectangle("pink", 140, 5)
pen.penup()
pen.goto(-70, 10)
draw_rectangle("pink", 140, 5)
# Saad
# Function to add decorations
def add_decorations():
    pen.color("red")
    pen.penup()
    pen.goto(-80, -50)
    pen.pendown()
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

    pen.penup()
    pen.goto(-40, -50)
    pen.pendown()
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

    pen.penup()
    pen.goto(40, -50)
    pen.pendown()
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

    pen.penup()
    pen.goto(80, -50)
    pen.pendown()
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

# Add decorations to the cake
add_decorations()

# Function to draw a candle with a flame
def draw_candle(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.forward(10)
    pen.left(90)
    pen.forward(30)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(30)
    pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(x + 5, y + 30)
    pen.pendown()
    pen.color("orange")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

# Draw candles on the top layer of the cake
draw_candle(-45, 20)
draw_candle(-7, 20)
draw_candle(30, 20)

# Move the turtle back to (0, 0)
pen.penup()
pen.goto(0, 0)
pen.hideturtle()  # Hide the turtle after drawing

# Keep the window open until clicked
screen.exitonclick()