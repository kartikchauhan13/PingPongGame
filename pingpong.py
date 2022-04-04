import turtle
import winsound

#game screen
win=turtle.Screen()
win.title("Ping Pong Game")
win.setup(width=800,height=600)
win.bgcolor("green")
win.tracer(0)

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("player a : 0 player b : 0",align="center" ,font=("Courier",20,"italic") )
#paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("cyan")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("pink")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.dx=0.5
ball.dy=-0.5

#paddle up
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

#paddle down function
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#paddle b up 
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
      
#paddle b down
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")


#score
score_a=0
score_b=0





#game loop
while True:
    win.update()

    #move the ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)

    #border check upside
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=  -1
    
    #border check down
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=  -1

    #border check left
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=  -1
        score_b+=1
        pen.clear()
        pen.write("player a : {} player b : {}".format(score_a,score_b),align="center" ,font=("Courier",20,"italic") )
        
    #border check right
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=  -1
        score_a+=1
        pen.clear()
        pen.write("player a : {} player b : {}".format(score_a,score_b),align="center" ,font=("Courier",20,"italic") )
    #paddle ball collisions
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor() +50) and (ball.ycor()>paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("sfx-boing8.mp3",winsound.SND_ASYNC)
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor() +50) and (ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("sfx-boing8.mp3",winsound.SND_ASYNC)

    
