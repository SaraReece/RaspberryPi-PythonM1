#!/bin/python3

# Import library code
from p5 import *
from random import randint

# Setup global variables
screen_size = 400
rocket_y = screen_size
burn = 100 #burn rate/frame
orbit_radius = 250
orbit_y = screen_size - orbit_radius

# The draw_rocket function goes here
def draw_rocket():

  global rocket_y, fuel, burn

  #only move the rocket if it has fuel
  if fuel >= burn and rocket_y > orbit_y:
    rocket_y -= 1 #Move the rocket
    fuel -= burn #Burn fuel
    print('Fuel left: ', fuel)
  # for loop to draw flames 
  no_stroke()
  for i in range(25): # Draw 25 burning exhaust ellipses
    fill(255, 255 - i * 10, 0) # creates a cool flame look fade from yellow to red
    ellipse(width/2, rocket_y + i, 8, 3)
  # create exhaust
  fill(200, 200, 200, 100) #Transparent grey
  for i in range(20): #Draw 20 random smoke ellipses
    ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))
    
  #not enough fuel for launch
  if fuel < burn and rocket_y > orbit_y: #No more fuel and not in orbit
    tint(255, 0, 0) #Failure
  elif fuel < 1000 and rocket_y <= orbit_y:
    tint(0, 255, 0) #Success
  elif fuel >= 1000 and rocket_y <= orbit_y:
   tint(255, 200, 0) #Too much fuel
  
  
  
  
  # set images dimesions
  image(rocket, width/2, rocket_y, 64, 64)
  #Don't bleed tint to planet
  no_tint()

# The draw_background function goes here
def draw_background():
  # set background to black
  background(0)
  #draw planet
  image_mode(CENTER)
  image(planet, width/2, height, 300, 300)
  #draw orbit
  no_fill() #Turn off any fill
  stroke(255) #Set a white stroke
  stroke_weight(2)
  ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)
  #draw rocket
  draw_rocket()
  
  

def setup():
  # set the screen size
  size(screen_size, screen_size)# set screensize
  # start the rocket at the bottom
  rocket_y = screen_size
  # Make sure planet and rocket are global
  global planet, rocket
  planet = load_image('purple_planet.png')
  rocket = load_image('rocket.png')


def draw():
  # Things to do in every frame
  draw_background()
  
fuel = int(input('Yo how many KG of fuel you want to use?'))  
run()
