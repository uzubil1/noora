import turtle as t

def pixel():

    i=0
    while i<4:
        t.forward(30)
        t.left(90)
        i=i+1
      
def row(): #!
    i=0
    while i <20:
        pixel()
        t.forward(30)
        i=i+1


def column():
    i=0
    while i <5:
        t.down()
        row()
        xpos = t.xcor()
        ypos = t.ycor()
        t.up()
        t.goto(-int(xpos), int(ypos-30))
        i = i+1

def main():
    t.speed(0)
    t.up()
    t.goto(-300,300)
    t.down()
    t.color("blue")
    column()
    input("ener enythinhg")

    t.done() #!

if __name__=="__main__":
    main()