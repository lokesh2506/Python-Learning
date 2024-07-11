import turtle
import random
import math
scr=turtle.Screen()
scr.setup(800,800)
scr.title("space fighter")
scr.bgcolor("black")


player_vertices=((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18,5),(15,0))
scr.register_shape("player",player_vertices)

player=turtle.Turtle()
player.shape("player")
player.color("white")
player.penup()
player.goto(0,0)

asteroid_vertices=((0,10),(5,7),(3,3),(10,0),(7,4),(8,-6),(0,-10),(-5,-5),(-7,-7),(-10,0),(-5,4),(-1,8))
scr.register_shape("asteroid",asteroid_vertices)

def get_heading_to(t1,t2):
    x1=t1.xcor()
    y1=t1.ycor()

    x2=t2.xcor()
    y2=t2.ycor()
    heading=math.atan2(y1-y2,x1-x2)
    heading=heading*180.0/3.14159
    return heading


asteroids=[]
for i in range(5):
    asteroid=turtle.Turtle()
    asteroid.shape("asteroid")
    asteroid.color("brown")
    asteroid.penup()
    asteroid.speed=random.randint(2,10)/100
    heading=random.randint(0,360)
    distance=random.randint(400,600)
    asteroid.setheading(heading)
    asteroid.forward(distance)
    asteroid.setheading(get_heading_to(player,asteroid))
    asteroids.append(asteroid)


missiles=[]
for i in range(3):
    missile=turtle.Turtle()
    missile.shape("arrow")
    missile.color("red")
    missile.penup()
    missile.goto(0,0)
    missile.speed(10)
    missile.state="ready"
    missiles.append(missile)
    missile.hideturtle()
  


pen=turtle.Turtle()
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.goto(0,370)
pen.write("Score : 0",font=("arial"))
pen.hideturtle()


def left_turn():
    player.left(8)

def right_turn():
    player.right(8)

def fire_missile():
    for missile in missiles:
        if missile.state=="ready":
            missile.goto(0,0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state="fire"
            break

scr.listen()
scr.onkeypress(left_turn,"Left")
scr.onkeypress(right_turn,"Right")
scr.onkeypress(fire_missile,"space")


while True:
    
    for missile in missiles:
        if missile.state=="fire":
            missile.fd(missile.speed)
            if missile.xcor()>400 or missile.xcor()<-400 or missile.ycor()>400 or missile.ycor()<-400:
                missile.hideturtle()
                missile.state="ready"
    
