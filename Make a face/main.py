#!/bin/python3

from p5 import *

def setup():
  # Put code to run once here
  size(400, 400) # width and height

def draw():
  # Put code to run every frame here
  background(255, 255, 255) # move under draw() to reset the drawing every frame
  grid() # add a # to the beginning of this line to hide the grid
  # face shape
  ellipse(width/2, height/2, 300, 200)
  # Add eyes
  fill(234, 0, 254)
  eye_size =80
  ellipse(160, 180, eye_size, eye_size) #x, y, width, height
  ellipse(240, 180, eye_size, eye_size)
  # Mouth
  no_fill()
  fill(108, 200, 206)
  rect(152, 235, 96, 30) #Smaller blue rectangle
  no_stroke()
  ellipse(150, 250, 30, 30) #Left ear loop
  ellipse(250, 250, 30, 30) #Right ear loop
  fill(255, 255, 255)
  
  
  
# Keep this to run your code
run()