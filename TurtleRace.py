from turtle import *
import random

WIDTH = 500
HEIGHT = 500

NUM_TURTLES = 5

# Screen setup
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgpic("race.png")

# Turtle class
class turtle_racer(object):
  def __init__(self, color, position):
    self.position = position
    self.color = color
    self.turt = Turtle()
    self.turt.shape("turtle")
    self.turt.penup()
    self.turt.color(color)
    self.turt.setpos(position)
    self.turt.setheading(0)
    
  def move(self):
    random_pace = random.randint(-5,25)
    # move the x position, y position remains the same for a horizontal racetrack
    self.position = (self.position[0] + random_pace, self.position[1])
    self.turt.forward(random_pace)

def startGame():
  turtle_list = []
  colors = ["firebrick","sandybrown","gold","olivedrab","cornflowerblue"]
  
  # print colors for user to pick from
  print("The turtles racing today are: ")
  for color in colors:
    print(color),
  print('\n')
  
  # ask the use to pick a color turtle they think will win
  user_guess = input("Guess which turtle will win the race: ")
  
  # check if user guess is one of the racer colors
  for color in colors:
    while user_guess not in colors:
      user_guess = input("Guess an available racer: ")

  print("\nOff to the races!")
  
  # set up turtles at starting line
  start = -200
  for turt in range(0, NUM_TURTLES):
    new_position = start + turt*(HEIGHT)/NUM_TURTLES
    turtle_list.append(turtle_racer(colors[turt], (-230, new_position)))
    #turtle_list[turt].turt.showturtle()
    
  run = True
  
  # move turtles until one reaches the finish line
  while run: 
    for turt in turtle_list:
      turt.move()
      
      # save winning color in array
      max_color = []
      max_distance = 0
      
      for turt in turtle_list:
       # if x position is past finish line and greater than max_distance, or equal to max distance, then append to winning color array
        if turt.position[0] > 200 and turt.position[0] > max_distance:
          max_distance = turt.position[0]
          max_color.append(turt.color)
        elif turt.position[0] > 200 and turt.position[0] == max_distance:
          max_distance = turt.position[0]
          max_color.append(turt.color)
    
    # when one turtle crosses finish line, run is false and print winner
    if len(max_color) > 0:
      run = False
      for winner in max_color:
        if (winner == user_guess):
          print("\nYou guessed it! The winner is: ")
          print(winner) 
          print("!")
        else:
          print("\nBetter luck next time! The winner is: ")
          print(winner)
        
# main code
start = input('Press Y/y to begin the race!')
if (start == 'Y' or start == 'y'): 
  startGame()
else:
  print("Goodbye!")
  False
