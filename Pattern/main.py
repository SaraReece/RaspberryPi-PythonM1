#!/bin/python3

from p5 import *
from random import randint


def setup():
# Put code to run once here
  size(400, 400)
  background(50, 120, 205)
  frame_rate(3)

def shape_0():
 # rectangle 
  fill(color_r, color_g, color_b) 
  rect(size_a, size_b, cor_x, cor_y) 

def shape_1():
  # elipsis
  fill(color_r, color_g, color_b) 
  ellipse(size_a, size_b, cor_x, cor_y) 
 
def shape_2():
  # triangle
  fill(color_r, color_g, color_b) 
  rect(size_a, size_b, cor_x, cor_y, tri_a, tri_b) 
  

def draw():
  #declare globals so we can edit them
  global cor_x, cor_y, size_a, size_b, color_r, color_b, color_g, tri_a, tri_b
  
  # let's draw 15 shapes
  for i in range (15):
    # randomize what shapes are drawn first
    randDraw = randint(0, 2)
    # reset global variables
    cor_x = randint(0, 400)
    cor_y = randint(0, 400)
    size_a = randint(0, 400)
    size_b = randint(0, 400)
    color_r = randint(0, 255)
    color_g = randint(0, 255)
    color_b = randint(0, 255)
    #Now draw the shapes
    if randDraw == 0:
      shape_0()
    elif randDraw == 1:
      shape_1()
    elif randDraw == 2:
      #triangle get extra coordinate set
      tri_a = randint(0, 400)
      tri_b = randint(0, 400)
      shape_2()

  
# Keep this to run your code
run()
