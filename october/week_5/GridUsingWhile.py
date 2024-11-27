
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

def main():
    t.penup()
    t.goto(-300,300)
    t.pendown()
    row()
    t.done() #!

if __name__=="__main__":
    main()