import turtle as t


def draw_circle(radius):
    color="pink"
    if radius==0:
        return radius
    else:
        t.up()
        t.goto(0,-radius)
        t.down()
        t.pencolor(color)
        t.circle(radius)
        draw_circle(radius-10)


def main():
    radius = 100
    draw_circle(radius)
    t.done()


main()