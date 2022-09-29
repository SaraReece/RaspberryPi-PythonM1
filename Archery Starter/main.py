#!/bin/python3

# Import library code
from p5 import *
from math import *
from random import randint

# The mouse_pressed function goes here
def mouse_pressed():
  # Scoring outer = 50, innter = 200, bullseye = 500 otherwise nada
  if hit_color == outer:
    print ('You hit the outer circle, 50 points!')
  elif hit_color == inner:
    print('You hit the inner circle, 200 points!')
  elif hit_color == bullseye:
    print('You hit the bullseye, 500 points!')
  else:
    print('You missed! No points!')
  
# The shoot_arrow function goes here
def shoot_arrow():
  # make hit_color a global variable
  global hit_color
  # var to hold random number between 100-300 to get coordinates
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  #Save the color before drawing
  hit_color = get (arrow_x, arrow_y)
  #draw the arrow at the random coordinate
  ellipse(arrow_x, arrow_y, 15, 15)

def setup():
# Setup your game here
  size(400, 400) # width and height
  frame_rate(2)
  
def draw():
  # make outer, inner, and bullseye global
  global outer, inner, bullseye
# Things to do in every frame
  sky = color(92, 204, 206) # Lighter blue
  grass = color(149, 212, 122) # Green
  wood = color(145, 96, 51) # Brown
  outer = color(0, 120, 180) # Darker blue
  inner = color(210, 60, 60) # Red
  bullseye = color(220, 200, 0) #Yellow
  no_stroke() # rectangle will not have black outline around boxes
  # draw sky
  fill(sky)
  rect(0, 0, 400, 250)
  # draw grass
  fill(grass)
  rect(0, 250, 400, 150)
  #draw stand for target
  fill(wood) 
  triangle(150, 350, 200, 150, 250, 350)
  #draw outer most circle of target
  fill(outer)
  ellipse(200, 200, 170, 170)
  #draw inner circle
  fill(inner)
  ellipse(200, 200, 110, 110) #Inner circle
  #Bullseye
  fill(bullseye)
  ellipse(200, 200, 30, 30) #Bullseye
  #draw error
  fill(wood)
  shoot_arrow()
  
  
  
# Keep this to run your code
run()
