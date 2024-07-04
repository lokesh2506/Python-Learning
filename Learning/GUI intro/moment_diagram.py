import turtle

scr=turtle.Screen()
scr.title("snake movement")
scr.setup(800,800)
scr.bgcolor("blue")


snake=turtle.Turtle()
snake.color("white")
snake.shape("square")

#it defines the shape size
snake.shapesize(5,1)

snake.penup()
snake.goto(-350,0)

def plyr_up():
    snake.shapesize(5,1)
    y=snake.ycor()  # it return value of y cord present of shape
    y+=20
    snake.sety(y)  # now we set new value for shape in y cord
    
def plyr_down():
    snake.shapesize(5,1)
    y=snake.ycor()
    y-=20
    snake.sety(y)

def plyr_right():
    snake.shapesize(1,5)
    x=snake.xcor()  # it return value of y cord present of shape
    x+=20
    snake.setx(x)  # now we set new value for shape in y cord
    
def plyr_left():
    snake.shapesize(1,5)
    x=snake.xcor()
    x-=20
    snake.setx(x)

scr.listen()
scr.onkeypress(plyr_up,"Up")
scr.onkeypress(plyr_down,"Down")
scr.onkeypress(plyr_right,"Right")
scr.onkeypress(plyr_left,"Left")
