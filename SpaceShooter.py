#!/bin/python3
import turtle as t
import random
import time

def startScreen():
  t.ht()
  t.pu()
  t.goto(0,50)
  t.color("white")
  t.write('Space Shooter', align='center',
          font=('Comic Sans', 34))
  t.ht()
  t.pu()
  t.goto(0,-20)
  t.color('white')
  t.write('Click to Start', align='center',
          font=('Deja Vu Sans Mono', 24, 'bold'))
  t.fillcolor('maroon')
  t.write('Click to Start', align='center',
          font=('Deja Vu Sans Mono', 24, 'bold'))
          
def setUpPlayer():
  p.pu()
  p.goto(0,-100)
  p.st()
  p.shape("spaceship.png")
  p.color("orange")
  p.fillcolor("silver")
  p.setheading(90)

def initSpawn():
  global round
  for i in range(initial_invaders):
    invaders.append(makeEvilInvaders())
  round+=1
  
def putStars():
  for s in range(50):
    size = random.randint(1,2)
    s = t.Turtle()
    stars.append(s)
    s.speed(0)
    s.pu()
    s.ht()
    s.color('white')
    s.circle(size)
    size = random.randrange(1,2)
    x = random.randint(-190, 190)  
    y = random.randint(-190, 190)
    s.goto(x,y)
    s.begin_fill()
    s.pendown()
    s.circle(size)
    s.penup()
    s.end_fill()
  
def playGame(x=0,y=0):
  t.clear()
  t.ht()
  screen.bgcolor("midnight blue")
  putStars()
  showScore()
  showLives()
  setUpPlayer()
  initSpawn()
  #makeEvilBoss()
  # turn of click after first click
  screen.onclick(None)
    
def showScore():
  global s
  s.pu()
  s.ht()
  s.color('white')
  s.goto(150,180)
  s.pd()
  s.write("Score: 0", align='center',font=('Comic Sans', 14, 'bold'))
  return s

def showLives():
  global life
  life.pu()
  life.ht()
  life.color('chartreuse')
  life.goto(-150,180)
  life.pd()
  life.write("Lives: 5", align='center',font=('Comic Sans', 14, 'bold'))
  return life
  
def make_laser():
  l = t.Turtle()
  l.speed(0)
  l.ht()
  l.color("yellow")
  l.shape("laser")
  l.penup()
  l.left(90)
  l.goto(p.pos())
  l.forward(20)
  l.st()
  return l

def fire_laser():
  laser = make_laser()
  lasers.append(laser)
    
def left():
  x = p.xcor()
  if (x > -200):
    x -= 10
    p.setx(x)
  
def right():
  x = p.xcor()
  if (x < 200):
    x += 10
    p.setx(x)

def down():
  y = p.ycor()
  if (y > -200):
    y -= 10
    p.sety(y)
    
def up():
  y = p.ycor()
  if (y < 200):
    y += 10
    p.sety(y)
    
def makeEvilInvaders():
  e = t.Turtle()
  e.ht()
  e.penup()
  e.shape('space_invader.png')
  e.pencolor('red')
  e.speed(0)
  x = random.randint(-190, 190)
  y = 190
  e.goto(x, y)
  e.right(90)
  e.st()
  return e
  
def makeEvilBoss():
  b = t.Turtle()
  b.st()
  b.goto(0,0)
  b.color('green')
  b.begin_fill()
  b.circle(50)
  b.end_fill()
  
def moveLasers():
    # update missiles
  for l in lasers[:]:
    y = l.ycor()
    if y < 200:
      l.sety(y + 15)
    else: # this missile is done
      l.hideturtle()
      lasers.remove(l)
      
def moveInvaders():
  for i in invaders[:]:
    y = i.ycor()
    if y > -200:
      i.sety(y - random.randint(0,5))
    else: # this invader is done
      i.hideturtle()
      invaders.remove(i)

def checkLaserHits():
  global score, s
  for l in lasers[:]:
    for i in invaders[:]:
      if l.distance(i) < 10:
        #print("lasered")
        score+=1
        s.clear()
        s.write("Score: {}".format(score), align='center',font=('Comic Sans', 14, 'bold'))
        i.ht()
        invaders.remove(i)

def checkEnemyCollision():
  global lives, life
  for i in invaders[:]:
    if p.distance(i) < 10:
      lives-=1
      life.clear()
      life.write("Lives: {}".format(lives), align='center',font=('Comic Sans', 14, 'bold'))
      p.ht()
      time.sleep(1)
      p.goto(0,-100)
      p.st()

def nextRound():
  global round
  if ((len(invaders) == 0) and (round > 1)):
    #print("round is: ",round)
    round+=1
    for i in range(initial_invaders+(round*2)):
      invaders.append(makeEvilInvaders())
  
#-------- MAIN CODE ----------#
screen = t.Screen()
screen.setup(400,400)
screen.bgcolor("dark slate blue")
screen.register_shape("laser", ((1, 0), (-1, 0), (-1, -10), (1, -10)))
screen.addshape("spaceship.png")
screen.addshape("space_invader.png")

startScreen()

# player turtle
p = t.Turtle()
p.ht()

# score turtle
s = t.Turtle()
s.ht()
life = t.Turtle()
life.ht()

# screen
screen.update()
screen.listen()
screen.onclick(playGame)

screen.onkey(left, 'left')
screen.onkey(right, 'right')
screen.onkey(up, 'up')
screen.onkey(down, 'down')
screen.onkey(fire_laser, ' ')

# variables 
stars = []

lives = 5
score = 0
round = 1

laser_timer = 0
lasers = []

initial_invaders = 5
invaders = []

# GAME LOOP
while True:
  moveLasers()
  moveInvaders()
  checkLaserHits()
  checkEnemyCollision()
  nextRound()
  if lives==0:
    break
  screen.update()
  
