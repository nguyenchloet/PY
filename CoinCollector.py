import turtle
import random
import time

# variables
# NON CONSTANT
score = 0
timeLimit = 60
startTime = time.time()

# all capitals = CONSTANT = not changing
ALIGN = "center"
FONT = ("Courier",15,"bold")

# screen setup
screen = turtle.Screen()
#tracer affects animation and hides images
#screen.tracer(0)
screen.setup(width=400,height=400)
screen.bgcolor("thistle")

screen.addshape('fox.png')
screen.addshape('coin.png')

# score turtle who keeps track of our score variable
scoreTurtle = turtle.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.penup()
scoreTurtle.color("medium blue")
scoreTurtle.goto(-100,150)
scoreTurtle.write("Score: 0", align=ALIGN, font=FONT)

# timer 
timer = turtle.Turtle()
timer.ht()
timer.tracer(0)
timer.penup()
timer.color("crimson")
timer.goto(100,150)
timer.write("Timer: {}".format(timeLimit), align=ALIGN, font=FONT)

# fox player
fox = turtle.Turtle()
fox.shape("fox.png")
fox.color("dark orange")
fox.penup()
fox.setheading(90)

# coin object
coin = turtle.Turtle()
coin.shape("coin.png")
coin.penup()
x = random.randint(-180,180)
y = random.randint(-180,180)
coin.goto(x,y)

# fox movement definitions
def moveUp():
  if fox.ycor() < 200:
    fox.forward(10)
  
def moveDown():
  if fox.ycor() > -200:
    fox.backward(10)
  
def moveLeft():
  (x,y) = fox.pos()
  if x > -200:
    fox.setx(x-10)
  
def moveRight():
  (x,y) = fox.pos()
  if x < 200:
    fox.setx(x+10)
  
# keyboard binding
screen.listen()
screen.onkey(moveUp, "up")
screen.onkey(moveDown, "down")
screen.onkey(moveLeft, "left")
screen.onkey(moveRight, "right")

# main loop for our game
while True:
  screen.update()
  
  # if the fox and coin touch eachother / collide, 
  #then move coin to new random spot and add point to score
  if fox.distance(coin) < 40:
    coin.hideturtle()
    x = random.randint(-180,180)
    y = random.randint(-180,180)
    coin.goto(x,y)
    coin.showturtle()
    # increment score    
    score+=1
    scoreTurtle.clear()
    scoreTurtle.write("Score: {}".format(score), align=ALIGN, font=FONT)
    
  #timer countdown
  timePassed = int(time.time() - startTime)
  timer.clear()
  timer.write("Timer: {}".format(timeLimit - timePassed), align=ALIGN, font=FONT)
  
  # game over when timer runs out (plus 1 second to show 0)
  if (timePassed > timeLimit):
    break;
 
# outside of the main while loop
print("Game Over!")
