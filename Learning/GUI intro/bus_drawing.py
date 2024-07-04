import turtle

scr=turtle.Screen()
scr.setup(800,800)
scr.title("Bus Drawing")
scr.bgcolor("lightblue")

#bus outline
pen=turtle.Turtle()
pen.shape("circle")
pen.hideturtle()
pen.color("yellow")
pen.pensize(5)


pen.penup()
pen.goto(-300,100)
pen.pendown()
pen.fillcolor("yellow")
pen.begin_fill()
for i in range(2):
    pen.fd(600)
    pen.rt(90)
    pen.fd(200)
    pen.rt(90)


pen.end_fill()
pen.hideturtle()


#wheel1

wheel1=turtle.Turtle()

wheel1.hideturtle()
#wheel1.shape("circle")
wheel1.color("black")
wheel1.pensize(10)
wheel1.penup()
wheel1.goto(-200,-150)
wheel1.pendown()
wheel1.fillcolor("black")
wheel1.begin_fill()
wheel1.circle(50)
wheel1.end_fill()
wheel1.hideturtle()

#wheel2

wheel2=turtle.Turtle()
#wheel2.shape("circle")
wheel2.hideturtle()
wheel2.color("black")
wheel2.pensize(10)
wheel2.penup()
wheel2.goto(200,-150)
wheel2.pendown()
wheel2.fillcolor("black")
wheel2.begin_fill()
wheel2.circle(50)
wheel2.end_fill()
wheel2.hideturtle()


#window

win1=turtle.Turtle()
#win1.shape("circle")
win1.hideturtle()
win1.color("lightblue")
win1.pensize(10)
win1.penup()
win1.goto(50,-0)
win1.pendown()
win1.fillcolor("lightblue")
win1.begin_fill()
for i in range(2):
    win1.fd(50)
    win1.lt(90)
    win1.fd(70)
    win1.lt(90)
win1.end_fill()
win1.hideturtle()



win2=turtle.Turtle()
#win2.shape("circle")
win2.hideturtle()
win2.color("lightblue")
win2.pensize(10)
win2.penup()
win2.goto(200,-0)
win2.pendown()
win2.fillcolor("lightblue")
win2.begin_fill()
for i in range(2):
    win2.fd(50)
    win2.lt(90)
    win2.fd(70)
    win2.lt(90)
win2.end_fill()
win2.hideturtle()


win3=turtle.Turtle()
#win3.shape("circle")
win3.hideturtle()
win3.color("lightblue")
win3.pensize(10)
win3.penup()
win3.goto(-100,0)
win3.pendown()
win3.fillcolor("lightblue")
win3.begin_fill()
for i in range(2):
    win3.fd(50)
    win3.lt(90)
    win3.fd(70)
    win3.lt(90)
win3.end_fill()
win3.hideturtle()


win4=turtle.Turtle()
#win4.shape("circle")
win4.hideturtle()
win4.color("lightblue")
win4.pensize(10)
win4.penup()
win4.goto(-250,0)
win4.pendown()
win4.fillcolor("lightblue")
win4.begin_fill()
for i in range(2):
    win4.fd(50)
    win4.lt(90)
    win4.fd(70)
    win4.lt(90)
win4.end_fill()
win4.hideturtle()
