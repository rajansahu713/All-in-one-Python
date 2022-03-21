import turtle
import time
# make a read color heart

pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(111)
    curve()
    pen.left(120)
    curve()
    pen.forward(111)
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color('lightgreen')
    pen.write('I Love you', font=('Arial', 24, 'normal'))
    time.sleep(3)

heart()
txt()
turtle.ht()