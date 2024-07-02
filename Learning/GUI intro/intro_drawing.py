import turtle

scr=turtle.Screen()
scr.bgcolor("white")
scr.setup(600,600)
scr.title("intro")

# creat the drawing

pen=turtle.Turtle()
pen.pensize(5)
pen.color("black")
pen.shape("turtle")

#crete a first box

pen.fillcolor("yellow")
pen.begin_fill()

for i in range(4):
    pen.forward(200) #200px to move forward
    pen.right(90) #90 degree to turn

pen.end_fill()


pen.fillcolor("lightgreen")
pen.begin_fill()

for i in range(4):
    pen.fd(200) #200px to move forward
    pen.lt(90) #90 degree to turn

pen.end_fill()

#fd - forward
#right - rt
#left -lt

pen.fillcolor("red")
pen.begin_fill()

for i in range(4):
    pen.fd(-200) #200px to move forward
    pen.rt(90) #90 degree to turn

pen.end_fill()



pen.fillcolor("lightblue")
pen.begin_fill()

for i in range(4):
    pen.fd(-200) #200px to move forward
    pen.lt(90) #90 degree to turn

pen.end_fill()
