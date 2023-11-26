import turtle

T = turtle.Turtle()
T.screen.bgcolor("black")
T.pensize(3)
T.color("green")
T.left(90)
T.backward(100)
T.speed(300)
T.shape("turtle")

def tree(i):
    if i<15:
        return
    else:
        T.forward(i)
        T.color("green")
        T.circle(2)
        T.color("green")
        T.left(30)
        tree(3* i/4)
        T.right(60)
        tree(3* i/4)
        T.left(30)
        T.backward(i)

tree(100)
turtle.done()