
import turtle as t


def triangle():
    t.penup()
    t.goto(10,50)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.forward(25)
    t.right(120)
    t.forward(25)
    t.right(120)
    t.forward(25)
    t.right(120)
    t.end_fill()


triangle()
t.right(90)

triangle()
t.right(90)


triangle()
t.right(90)


triangle()
t.right(90)