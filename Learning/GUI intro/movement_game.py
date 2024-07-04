import turtle
import random

scr=turtle.Screen()
scr.setup(300,600)
scr.bgpic("bg.gif")
scr.title("game")



#register the new shape as picture
scr.register_shape("cc.gif")
ply=turtle.Turtle()
ply.shape("cc.gif")
ply.penup()
ply.goto(-90,-250)


plyr=turtle.Turtle()
plyr.shape("cc.gif")
plyr.penup()
x=random.randint(-150,150)
plyr.goto(x,250)


def left_mov():
    x=ply.xcor()
    x-=10
    ply.setx(x)

def right_mov():
    x=ply.xcor()
    x+=10
    ply.setx(x)


scr.listen()
scr.onkeypress(left_mov,"Left")
scr.onkeypress(right_mov,"Right")


while True:
    y=plyr.ycor()
    y-=3
    plyr.sety(y)
