import turtle
import random
import math

scr=turtle.Screen()
scr.setup(800,800)
scr.title("Space invader")
scr.bgpic("bgpic1.gif")
scr.tracer(0)

scr.register_shape("alien.gif")
scr.register_shape("rocket.gif")


plyr=turtle.Turtle()
plyr.shape("rocket.gif")
plyr.penup()
plyr.goto(0,-300)

score=0

bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.goto(0,-245)
bullet.setheading(90)
bullet.hideturtle()
bulletspeed=2

enemyspeed=0.2

enemies=[]
for i in range(5):
    ene=turtle.Turtle()
    ene.shape("alien.gif")
    ene.penup()
    x=random.randint(-340,340)
    y=random.randint(250,350)
    ene.goto(x,y)
    enemies.append(ene)


pen=turtle.Turtle()
pen.color("yellow")
pen.penup()
pen.goto(-320,350)

pen.write("Score : 0",align="center",font=("arial",22,"bold"))
pen.hideturtle()
bulletstate="ready"

def left_side():
    x=plyr.xcor()
    x-=20
    if x <-340:
        x=-340
    plyr.setx(x)

def right_side():
    x=plyr.xcor()
    x+=20
    if x >340:
        x=340
    plyr.setx(x)

def fire_bullet():
    bullet.showturtle()
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        x=plyr.xcor()
        y=plyr.ycor()
        bullet.goto(x,y+60)
        
def iscollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<40:
        return True
    else:
        return False

scr.listen()
scr.onkeypress(left_side,"Left")
scr.onkeypress(right_side,"Right")
scr.onkeypress(fire_bullet,"space")


while True:
    scr.update()
    for e in enemies:
        x=e.xcor()
        x+=enemyspeed
        e.setx(x)

        if x>370 or x<-370:
            for e in enemies:
                y=e.ycor()
                y-=100
                e.sety(y)
                enemyspeed*=-1
        if iscollision(bullet,e):
            bullet.hideturtle()
            bulletstate="ready"
            bullet.goto(0,-500)
            x=random.randint(-340,340)
            y=random.randint(250,350)
            e.goto(x,y)
            score+=10
            pen.clear()
            pen.write("Score : {}".format(score),align="center",font=("arial",22,"bold"))

        if iscollision(plyr,e):
            plyr.hideturtle()
            e.hideturtle()
            exit()
            print("game over")
        
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
                       
    if bullet.ycor()>350:
        bullet.hideturtle()
        bulletstate="ready"
        
        
        
