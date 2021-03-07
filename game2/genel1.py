import turtle as tr
from random import randint as rd
from playsound import playsound as py
#for screen
screen=tr.Screen()
screen.screensize(600,600)
screen.title("turtle lari yakala")
screen.bgcolor("blue")
screen.bgpic("img_1.png")
screen.tracer(2)

#for gamer
gamer=tr.Turtle()
gamer.color("white")
gamer.shape("triangle")
gamer.shapesize(3)
gamer.penup()
speed=1
score=0

yazi_puan=turtle.Turtle()
yazi_puan.speed(0)
yazi_puan.color("white")
yazi_puan.shape("square")
yazi_puan.penup()
yazi_puan.hideturtle()
yazi_puan.goto(-200,200)
yazi_puan.write(f"Puan {score}",align="center",font={"Arial-Black",24})

speed_puan=turtle.Turtle()
speed_puan.speed(0)
speed_puan.color("white ")
speed_puan.shape("square")
speed_puan.penup()
speed_puan.hideturtle()
speed_puan.goto(200,200)
speed_puan.write(f"Hız {speed}",align="center",font={"Arial-Black",24})
#fonc
def soladon():
    gamer.left(20)
def sagadon():
    gamer.right(20)
def artir():
    global speed
    speed+=1
    speed_puan.clear()
    speed_puan.write(f"Hız {speed}", align="center", font={"Courier", 24})
def azalt():
    global speed
    speed-=1
    speed_puan.clear()
    speed_puan.write(f"Hız {speed}", align="center", font={"Courier", 24})

screen.listen()
screen.onkey(soladon ,"Left")
screen.onkey(sagadon,"Right")

screen.onkey(artir,"Up")
screen.onkey(azalt,"Down")
max_hedef=5
hedefler=[]
for i in range(5):
    hedefler.append(turtle.Turtle())
    hedefler[i].penup()
    hedefler[i].shape("turtle")
    hedefler[i].color("green")
    hedefler[i].speed(0)
    hedefler[i].setposition(rd(-300, 300), rd(-300, 300))
while True:
    gamer.forward(speed)
    if gamer.xcor()>300 or  gamer.xcor()<-300:
        gamer.right(180)
    elif gamer.ycor()>300 or gamer.ycor()<-300:
        gamer.left(180)
    for i in range(5):
        hedefler[i].forward(1)
        if  gamer.distance(hedefler[i])<35:
            hedefler[i].setposition(rd(-300, 300), rd(-300, 300))
            hedefler[i].right(rd(0,360))
            score+=1
            yazi_puan.clear()
            yazi_puan.write(f"Puan {score}", align="center", font={"Courier", 24})
        if hedefler[i].xcor()<-500 or hedefler[i].xcor()>500:
            hedefler[i].right(rd(150,250))
        elif hedefler[i].ycor()<-500 or hedefler[i].ycor()>500:
            hedefler[i].left(rd(150,250))





